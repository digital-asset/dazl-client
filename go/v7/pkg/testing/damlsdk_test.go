package testing

import (
	"testing"
)

func TestDefault(t *testing.T) {
	sdk, err := Default()
	if err != nil {
		t.Fatalf("error resolving the default SDK: %v", err)
	}
	if sdk.Home == "" {
		t.Fatal("The DAML SDK does not appear to be installed")
	}

	t.Logf("The DAML SDK is installed at: %v", sdk.Home)
	t.Logf("The default version is: %v", sdk.DefaultVersion)
}
