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

func TestExamplePython(t *testing.T) {
	t.Cleanup(cleanupSnapshots)

	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(getCwd(t), "python"),
		})
	integration.ProgramTest(t, &test)
}
