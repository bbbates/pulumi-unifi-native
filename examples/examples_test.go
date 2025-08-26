package examples

import (
	"context"
	"fmt"
	"github.com/golang/glog"
	"github.com/testcontainers/testcontainers-go"
	"github.com/testcontainers/testcontainers-go/network"
	"github.com/testcontainers/testcontainers-go/wait"
	"net/http"
	"os"
	"testing"
	"time"
)

const (
	UnifiImage = "jacobalberty/unifi:%s"
)

func TestMain(m *testing.M) {
	os.Exit(runAcceptanceTests(m))
}

func runAcceptanceTests(m *testing.M) int {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	nw, err := network.New(ctx)
	if err != nil {
		glog.Errorf("failed to create network: %s", err)
		panic(err)
	}
	defer func() {
		if err := nw.Remove(ctx); err != nil {
			glog.Errorf("failed to remove network: %s", err)
		}
	}()
	ctrRequest := testcontainers.ContainerRequest{
		Image:        fmt.Sprintf(UnifiImage, "v9"), // TODO: read this from env var or file
		ExposedPorts: []string{"8443/tcp"},
		WaitingFor:   wait.ForListeningPort("8443/tcp").WithStartupTimeout(time.Second * 30),
		Files: []testcontainers.ContainerFile{{
			HostFilePath:      "resources/scripts/init.d/demo-mode",
			ContainerFilePath: "/usr/local/unifi/init.d/demo-mode",
			FileMode:          0o644,
		}},
		Networks: []string{nw.Name},
	}

	ctr, err := testcontainers.GenericContainer(ctx, testcontainers.GenericContainerRequest{
		ContainerRequest: ctrRequest,
		Started:          true,
	})
	if err != nil {
		glog.Errorf("failed to start container: %s", err)
		panic(err)
	}

	defer func() {
		if err := ctr.Terminate(context.Background()); err != nil {
			panic(err)
		}
	}()

	hostname, err := ctr.Host(ctx)
	if err != nil {
		panic(err)
	}

	mappedPort, err := ctr.MappedPort(ctx, "8443")
	if err != nil {
		panic(err)
	}

	glog.Infof("Unifi controller started at %s:%s", hostname, mappedPort.Port())

	if err := setupEnvironment(fmt.Sprintf("%s:%s", hostname, mappedPort.Port())); err != nil {
		panic(err)
	}

	return m.Run()
}

func setupEnvironment(endpoint string) error {
	settings := map[string]string{
		"UNIFI_APIKEY":         "keykeykey",
		"UNIFI_ALLOW_INSECURE": "true",
		"UNIFI_API_HOST":       endpoint,
	}

	for name, value := range settings {
		if err := os.Setenv(name, value); err != nil {
			return err
		}
	}

	return nil
}

func TestWithUnifi(t *testing.T) {
	_, err := http.Get(fmt.Sprintf("https://%s", os.Getenv("UNIFI_API_HOST")))
	if err != nil {
		t.Errorf("error making request to unifi controller: %s", err)
		panic(err)
	}

}
