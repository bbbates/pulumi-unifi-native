package examples

import (
	"bytes"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"github.com/bmatcuk/go-vagrant"
	"net/http"
	"net/http/cookiejar"
	"os"
	"os/exec"
	"testing"
)

func TestMain(m *testing.M) {
	os.Exit(runAcceptanceTests(m))
}

func runAcceptanceTests(m *testing.M) int {
	vagrantClient, err := vagrant.NewVagrantClient("unifios")
	if err != nil {
		fmt.Printf("error creating vagrant client: %s", err)
		return 1
	}

	fmt.Printf("Bringing up UnifiOS test fixture...\n")
	upCmd := vagrantClient.Up()
	if err := upCmd.Run(); err != nil {
		fmt.Printf("error starting vagrant up: %s", err)
		return 2
	}
	if upCmd.Error != nil {
		fmt.Printf("error during vagrant up: %s", err)
		return 3
	}

	fmt.Printf("UnifiOS test fixture UP, initialising environment...\n")

	sshConfigCmd := vagrantClient.SSHConfig()
	if err := sshConfigCmd.Run(); err != nil {
		fmt.Printf("error getting vagrant ssh-config: %s", err)
		return 4
	}
	hostName := fmt.Sprintf("%s:11443", sshConfigCmd.Configs["default"].HostName)

	if err := setupEnvironment(hostName); err != nil {
		panic(err)
	}

	destroyCmd := vagrantClient.Destroy()
	defer func() {
		err := destroyCmd.Run()
		if err != nil {
			fmt.Printf("error during vagrant destroy - ** manual cleanup required before next test run **: %s", err)
		}
	}()

	// take a snapshot of the clean state
	snapshotErr := pushSnapshot()
	if snapshotErr != nil {
		fmt.Printf(snapshotErr.Error())
		return 5
	}

	fmt.Printf("UnifiOS fixture initial snapshot taken. Starting tests...\n")

	return m.Run()
}

func pushSnapshot() error {
	cmd := exec.Command("vagrant", "snapshot", "push")
	cmd.Dir = "unifios"
	if output, err := cmd.CombinedOutput(); err != nil {
		return fmt.Errorf("error creating vagrant snapshot: %s\nOutput: %s", err, string(output))
	}
	return nil
}

func setupEnvironment(endpoint string) error {
	apiKey, err := createSessionApiKey(endpoint)
	if err != nil {
		return fmt.Errorf("error creating api key: %s", err)
	}

	settings := map[string]string{
		"UNIFI_APIKEY":         apiKey,
		"UNIFI_ALLOW_INSECURE": "true",
		"UNIFI_API_HOST":       endpoint,
	}

	for name, value := range settings {
		if err := os.Setenv(name, value); err != nil {
			return err
		}
	}

	fmt.Printf("--- UnifiOS Test Fixture ---\nAPI Host: %s\nAPI Key: %s\n---------------------------\n\n", endpoint, apiKey)

	return nil
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

func TestWithUnifi(t *testing.T) {
	_, err := http.Get(fmt.Sprintf("https://%s", os.Getenv("UNIFI_API_HOST")))
	if err != nil {
		t.Errorf("error making request to unifi controller: %s", err)
		t.Fail()
	}
}

// TODO:
// - snapshot pop after each test
// - create API key for test suite, add to env
// - write tests
// - stop the need for sudo to bring up and destroy the VM
// - how to get vagrant logs to stdout for debugging?
