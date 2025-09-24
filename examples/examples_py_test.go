package examples

import (
	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
	"path/filepath"
	"testing"
)

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	basePython := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	return basePython
}

func TestExampleNetworksPython(t *testing.T) {
	t.Cleanup(cleanupSnapshots)

	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(getCwd(t), "python", "networks"),
		})
	integration.ProgramTest(t, &test)
}

func TestExampleDevicesPython(t *testing.T) {
	t.SkipNow()
	t.Cleanup(cleanupSnapshots)

	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(getCwd(t), "python", "devices"),
		})

	integration.ProgramTest(t, &test)
}

func TestExampleUsersPython(t *testing.T) {
	t.Cleanup(cleanupSnapshots)

	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(getCwd(t), "python", "users"),
		})
	integration.ProgramTest(t, &test)
}
