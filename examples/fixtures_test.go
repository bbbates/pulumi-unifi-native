package examples

import (
	"bytes"
	"crypto/tls"
	"encoding/json"
	"flag"
	"fmt"
	"github.com/bmatcuk/go-vagrant"
	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
	"net/http"
	"net/http/cookiejar"
	"os"
	"os/exec"
	"path/filepath"
	"testing"
)

var noSnapshots *bool

func TestMain(m *testing.M) {
	existingVmFlag := flag.Bool("existingfixture", false, "Use a running instance of a Unifios vagrant vm")
	noSnapshots = flag.Bool("nosnapshots", false, "Don't take or pop snapshots of the vagrant vm")
	flag.Parse()
	os.Exit(runAcceptanceTests(m, *existingVmFlag, *noSnapshots))
}

func runAcceptanceTests(m *testing.M, useExistingVm bool, noSnapshots bool) int {
	vagrantClient := vagrantClient()

	if !useExistingVm {
		fmt.Printf("Bringing up UnifiOS test fixture...\n")
		upCmd := vagrantClient.Up()
		if err := upCmd.Run(); err != nil {
			fmt.Printf("error starting vagrant up: %s", err)
			return 2
		}
		if upCmd.Error != nil {
			fmt.Printf("error during vagrant up: %s", upCmd.Error)
			return 3
		}

		destroyCmd := vagrantClient.Destroy()
		defer func() {
			err := destroyCmd.Run()
			if err != nil {
				fmt.Printf("error during vagrant destroy - ** manual cleanup required before next test run **: %s", err)
			}
		}()
	} else {
		fmt.Printf("Using existing Unifios VM fixture...\n")
	}

	if !noSnapshots {
		fmt.Printf("UnifiOS fixture up. Taking initial snapshot...\n")

		// take a snapshot of the clean state
		snapshotErr := pushSnapshot()
		if snapshotErr != nil {
			fmt.Printf(snapshotErr.Error())
			return 5
		}
	}

	fmt.Printf("UnifiOS fixture initial snapshot taken. Starting tests...\n")

	return m.Run()
}

func vagrantClient() *vagrant.VagrantClient {
	client, err := vagrant.NewVagrantClient("unifios")
	if err != nil {
		panic(err)
	}
	return client
}

func extractHostname(vagrantClient *vagrant.VagrantClient) (string, error) {
	sshConfigCmd := vagrantClient.SSHConfig()
	if err := sshConfigCmd.Run(); err != nil {
		return "", fmt.Errorf("error getting vagrant ssh-config: %s", err)
	}
	hostName := fmt.Sprintf("%s:11443", sshConfigCmd.Configs["default"].HostName)
	return hostName, nil
}

func pushSnapshot() error {
	cmd := exec.Command("vagrant", "snapshot", "push")
	cmd.Dir = "unifios"
	if output, err := cmd.CombinedOutput(); err != nil {
		return fmt.Errorf("error creating vagrant snapshot: %s\nOutput: %s", err, string(output))
	}
	return nil
}

func popSnapshot() error {
	cmd := exec.Command("vagrant", "snapshot", "pop")
	cmd.Dir = "unifios"
	fmt.Printf("Restoring vagrant snapshot...\n")
	if output, err := cmd.CombinedOutput(); err != nil {
		return fmt.Errorf("error restoring vagrant snapshot: %s\nOutput: %s", err, string(output))
	}
	return nil
}

func cleanupSnapshots() {
	if !*noSnapshots {
		err := popSnapshot()
		if err != nil {
			fmt.Printf("error popping snapshot - future test results may be inconsistent! %v", err)
		}
	}
}

func setupEnvironment() (string, string, error) {
	hostname, err := extractHostname(vagrantClient())
	if err != nil {
		return "", "", fmt.Errorf("error creating api key: %s", err)
	}
	apiKey, err := createSessionApiKey(hostname)
	if err != nil {
		return "", "", fmt.Errorf("error creating api key: %s", err)
	}

	fmt.Printf("%s <- %s\n", hostname, apiKey)

	return hostname, apiKey, nil
}

type LoginResponse struct {
	UniqueId string `json:"unique_id"`
}

type KeyResponseData struct {
	FullApiKey string `json:"full_api_key"`
}

type KeyResponse struct {
	Data KeyResponseData `json:"data"`
}

func createSessionApiKey(endpoint string) (string, error) {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: true, // required as we don't trust the test fixture TLS cert
		},
		Proxy: http.ProxyFromEnvironment,
	}
	cookieJar, err := cookiejar.New(nil)
	if err != nil {
		return "", err
	}
	client := &http.Client{Transport: tr, Jar: cookieJar}

	// Step 1: login
	buf := []byte(`{
		"username":"admin",
		"password":"SimpleIsBetter99!",
		"token":"",
		"rememberMe":false}`)

	loginRes, err := client.Post(fmt.Sprintf("https://%s/api/auth/login", endpoint),
		"application/json", bytes.NewBuffer(buf))
	if err != nil {
		return "", err
	}
	if loginRes.StatusCode != 200 {
		return "", fmt.Errorf("error logging in, status code: %d", loginRes.StatusCode)
	}

	csrfToken := loginRes.Header.Get("x-csrf-token")
	loginResponseBody := &LoginResponse{}
	decodeErr := json.NewDecoder(loginRes.Body).Decode(loginResponseBody)
	if decodeErr != nil {
		return "", fmt.Errorf("error decoding login result %s", decodeErr)
	}

	// Step 2: create API key
	keyReqBuf := []byte(`{
		"name":"test"
	}`)
	keyReq, err := http.NewRequest("POST",
		fmt.Sprintf("https://%s/proxy/users/api/v2/user/%s/keys", endpoint, loginResponseBody.UniqueId),
		bytes.NewBuffer(keyReqBuf))
	if err != nil {
		return "", err
	}

	keyReq.Header.Add("Content-Type", "application/json")
	keyReq.Header.Add("x-csrf-token", csrfToken)
	keyRes, err := client.Do(keyReq)
	if err != nil {
		return "", err
	}
	if keyRes.StatusCode != 200 {
		return "", fmt.Errorf("error creating api key, status code: %d", keyRes.StatusCode)
	}

	keyResponse := &KeyResponse{}
	keyDecodeErr := json.NewDecoder(keyRes.Body).Decode(keyResponse)
	if keyDecodeErr != nil {
		return "", fmt.Errorf("error decoding key post result %s", keyDecodeErr)
	}

	return keyResponse.Data.FullApiKey, nil
}

func getBaseOptions(t *testing.T) integration.ProgramTestOptions {
	hostname, apiKey, err := setupEnvironment()
	if err != nil {
		panic(err)
	}

	return integration.ProgramTestOptions{
		RunUpdateTest:        false,
		ExpectRefreshChanges: true,
		Config: map[string]string{
			"unifi-native:apiHost":       hostname,
			"unifi-native:allowInsecure": "true",
		},
		Secrets: map[string]string{
			"unifi-native:apiKey": apiKey,
		},
		// ensure the resource provider binary located in the bin directory is the one being tested
		Env: []string{fmt.Sprintf("PATH=%s:%s", filepath.Join(getCwd(t), "..", "bin"), os.Getenv("PATH")),
			// pass through proxy settings if they exist in the test environment
			fmt.Sprintf("HTTPS_PROXY=%s", os.Getenv("HTTPS_PROXY")),
			fmt.Sprintf("HTTP_PROXY=%s", os.Getenv("HTTP_PROXY")),
			"PULUMI_SKIP_UPDATE_CHECK=true",
		},
		DebugLogLevel: 3,
		DebugUpdates:  true,
		Verbose:       true,
	}
}

func getCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

// TODO:
// - snapshot pop after each test
// - create API key for test suite, add to env
// - write tests
// - stop the need for sudo to bring up and destroy the VM
// - how to get vagrant logs to stdout for debugging?
