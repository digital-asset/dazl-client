package testing

import (
	"errors"
	"fmt"
	"io/ioutil"
	"os/exec"
	"path"
	"sort"

	"github.com/blang/semver"
)

type DamlSDK struct {
	Home           string
	DefaultVersion *semver.Version
}

// Default returns parameters for DamlSDK as discovered by looking for the `daml` executable on the
// user's current `PATH`.
func Default() (sdk DamlSDK, err error) {
	if damlBin, err := exec.LookPath("daml"); err == nil {
		sdk.Home = path.Dir(path.Dir(damlBin))
	}

	// Try to populate the default version. The error is unused here.
	_ = sdk.ReadDefaultVersion()
	return
}

// InstalledVersions lists the locally available versions of the DAML SDK.
func (sdk DamlSDK) InstalledVersions() (versions semver.Versions) {
	files, err := ioutil.ReadDir(path.Join(sdk.Home, "sdk"))
	if err == nil {
		for _, f := range files {
			if f.IsDir() {
				v, err := semver.Parse(f.Name())
				if err == nil {
					versions = append(versions, v)
				}
			}
		}
	}
	sort.Sort(versions)
	return
}

// ReadDefaultVersion() fills in the DefaultVersion field for a DamlSDK.
func (sdk *DamlSDK) ReadDefaultVersion() error {
	if sdk.Home == "" {
		return errors.New("DamlSdk.Home is not set")
	}

	versions := sdk.InstalledVersions()
	if len(versions) == 0 {
		return fmt.Errorf("no SDK versions installed in %s", sdk.Home)
	}

	sdk.DefaultVersion = &versions[len(versions)-1]
	return nil
}
