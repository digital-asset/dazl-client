package testing

import (
	"testing"
)

func TestNewSandbox(t *testing.T) {
	t.Skip("This fixture appears to be buggy")

	options := SandboxOptions{}
	sandbox, err := NewSandbox(options)
	if err != nil {
		t.Errorf("Could not start a sandbox: %v", err)
	}
	defer sandbox.Stop()

	t.Logf("PID: %d\n", sandbox.ProcessId())
	t.Logf("SDK version: %v\n", sandbox.SDKVersion())
	t.Logf("Ledger ID: %s\n", sandbox.LedgerId())
}
