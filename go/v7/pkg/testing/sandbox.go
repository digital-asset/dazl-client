package testing

import (
	"context"
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"os"
	"os/exec"
	"path"
	"strconv"
	"time"

	"github.com/blang/semver"

	dazlclient "github.com/digital-asset/dazl-client/go/v7/pkg/client"
)

// SandboxOptions are launch options for starting a Sandbox.
type SandboxOptions struct {
	// Context optionally launches the Sandbox, managed by the given context.
	// If this context is terminated, the process is terminated.
	Context context.Context

	// ListenAddress is the address that the Sandbox will bind to. If
	// unspecified, 127.0.0.1 is used.
	ListenAddress net.IP

	// Port is the port that the Sandbox will bind to. If unspecified, the
	// default Ledger API port (6865) is used; if set to 0, a port will
	// automatically be assigned.
	Port *int

	// LedgerId is the ID of the created ledger. If unspecified, the
	// implementation may provide its own Ledger Id.
	LedgerId dazlclient.LedgerId

	// JDBCURL is the JDBC URL to connect to. If unspecified, an in-memory
	// database is used instead.
	JDBCURL string

	// SDKVersion is the version of the DAML SDK to use to launch the Sandbox.
	// Only Sandbox versions 1.0.0 or later are supported. The default version
	// is the most recent one available.
	SDKVersion *semver.Version

	// DamlHome is the path to a DAML SDK installation. If unspecified, it is
	// detected by looking for the `daml` command in the path.
	DamlHome string

	// LogPath is the place to pipe stdout/stderr to.
	LogPath string
}

// SandboxProcess represents a running instance of a Sandbox.
type SandboxProcess interface {
	Context() context.Context

	ListenAddress() net.IP

	// Port is the actual port that the Sandbox is using. If a sandbox was
	// created with SandboxOptions.Port as `0` or `nil`, Port() returns the
	// actual port that the process is listening on.
	Port() int

	// LedgerId returns the ledger id of the running Sandbox.
	LedgerId() dazlclient.LedgerId

	JDBCURL() string

	// DAML SDK version of the running Sandbox
	SDKVersion() semver.Version

	// PID of the Sandbox process
	ProcessId() int

	// Stop shuts down the Sandbox process. This method does _not_ block.
	Stop()
}

var _ SandboxProcess = (*sandboxProcess)(nil)


type sandboxProcess struct {
	context       context.Context
	listenAddress net.IP
	port          int
	portFile      string
	ledgerId      dazlclient.LedgerId
	jdbcURL       string
	sdkVersion    semver.Version
	damlHome      string
	logPath       string
	cmd           *exec.Cmd
	stopCh        chan struct{}
	errorCh       chan error
}

func (s *sandboxProcess) Context() context.Context {
	return s.context
}

// ListenAddress is the address
func (s *sandboxProcess) ListenAddress() net.IP {
	return s.listenAddress
}

func (s *sandboxProcess) Port() int {
	return s.port
}

func (s *sandboxProcess) LedgerId() dazlclient.LedgerId {
	return s.ledgerId
}

func (s *sandboxProcess) JDBCURL() string {
	return s.jdbcURL
}

func (s *sandboxProcess) SDKVersion() semver.Version {
	return s.sdkVersion
}

func (s *sandboxProcess) ProcessId() int {
	return s.cmd.Process.Pid
}

func (s *sandboxProcess) Stop() {
	s.stopCh <- struct{}{}
}

func portOrDefault(port *int) int {
	if port != nil {
		return *port
	} else {
		return 6865
	}
}

// NewSandbox creates a new Sandbox instance. The function blocks until the Sandbox has successfully
// been started, the port is open, and accepting connections, OR returns an error if this is not
// possible.
//
// See the documentation for SandboxOptions for information on default values that will be used if
// none are specified.
func NewSandbox(options SandboxOptions) (SandboxProcess, error) {
	var sdkVersion semver.Version
	if options.DamlHome == "" {
		defaultSDK, err := Default()
		if err != nil {
			return nil, err
		}

		options.DamlHome = defaultSDK.Home

		if options.SDKVersion == nil {
			defaultVersion := defaultSDK.DefaultVersion
			if defaultVersion != nil {
				sdkVersion = *defaultVersion
			}
		}
	}

	if options.Context == nil {
		options.Context = context.Background()
	}
	if options.ListenAddress == nil {
		options.ListenAddress = net.IPv4(127, 0, 0, 1)
	}

	s := &sandboxProcess{
		context:       options.Context,
		listenAddress: options.ListenAddress,
		port:          portOrDefault(options.Port),
		ledgerId:      options.LedgerId,
		jdbcURL:       options.JDBCURL,
		sdkVersion:    sdkVersion,
		damlHome:      options.DamlHome,
		stopCh:        make(chan struct{}),
		errorCh:       make(chan error),
	}

	// Now start the process in the background.
	go s.run()

	// Wait for the port to open
	if s.portFile != "" {
		// the port was randomized, so wait for the port file to appear before trying to connect
		port, err := s.waitForPortFile()
		if err != nil {
			s.Stop()
			return nil, err
		}

		s.port = port
	}

	var target string
	connectAddress := s.listenAddress
	if connectAddress.IsUnspecified() {
		target = fmt.Sprintf("%s:%d", net.IPv4(127, 0, 0, 1), s.port)
	} else {
		target = fmt.Sprintf("%s:%d", connectAddress, s.port)
	}

	ledgerId, err := dazlclient.GetLedgerId(options.Context, target)
	if err != nil {
		s.Stop()
		return nil, err
	}

	s.ledgerId = ledgerId
	return s, nil
}

// NewSandbox creates a new Sandbox instance with default parameters from the specified DAML SDK.
func (sdk DamlSDK) NewSandbox(options SandboxOptions) (s SandboxProcess, err error) {
	if options.DamlHome != "" {
		options.DamlHome = sdk.Home
	}
	if options.SDKVersion != nil {
		options.SDKVersion = sdk.DefaultVersion
	}

	return NewSandbox(options)
}

// The goroutine that monitors the Sandbox process that is launched. This function terminates when
// the process terminates.
func (s *sandboxProcess) run() {
	killCh := make(chan struct{})
	procEndedCh := make(chan struct{})

	if s.context == nil {
		s.cmd = exec.CommandContext(s.context, "java", s.args()...)
	} else {
		s.cmd = exec.Command("java", s.args()...)
	}

	writer := log.Writer()
	s.cmd.Stdout = writer
	s.cmd.Stderr = writer

	if err := s.cmd.Start(); err != nil {
		s.errorCh <- err
		return
	}

	go func() {
		_ = s.cmd.Wait()
		procEndedCh <- struct{}{}
	}()

	// Process management is "single-threaded" through this `for`/`select` statement, as process
	// management is inherently a racy thing.
	for {
		select {
		case <-s.stopCh:
			err := s.cmd.Process.Signal(os.Interrupt)
			if err != nil {
				s.errorCh <- err
			} else {
				// we successfully sent a signal; in five seconds we're going to lose patience and
				// pull the plug
				time.AfterFunc(5*time.Second, func() { killCh <- struct{}{} })
			}

		case <-killCh:
			_ = s.cmd.Process.Kill()

		case <-procEndedCh:
			// once the process has ended, there is nothing for us to do
			return
		}
	}
}

func (s *sandboxProcess) jar() string {
	return path.Join(s.damlHome, "sdk", s.sdkVersion.String(), "daml-sdk", "daml-sdk.jar")
}

func (s *sandboxProcess) args() []string {
	args := []string{
		"-jar", s.jar(),
		"sandbox-classic",
		"--address", s.listenAddress.String(),
	}

	if s.port == 0 {
		args = append(args, "--port-file", s.portFile)
	} else {
		args = append(args, "--port", strconv.Itoa(s.port))
	}

	if s.ledgerId != "" {
		args = append(args, "--ledgerid", string(s.ledgerId))
	}
	if s.jdbcURL != "" {
		args = append(args, "--sql-backend-jdbcurl", s.jdbcURL)
	}

	return args
}

func (s *sandboxProcess) waitForPortFile() (int, error) {
	ctx, cancelFn := context.WithCancel(s.context)
	time.AfterFunc(5*time.Second, cancelFn)
	t := time.NewTicker(100 * time.Millisecond)
	defer t.Stop()

	for {
		select {
		case <-t.C:
			bytes, err := ioutil.ReadFile(s.portFile)
			if err == nil {
				s := string(bytes)
				port, err := strconv.Atoi(s)
				if err == nil {
					return port, nil
				}
			}

		case <-ctx.Done():
			return 0, errors.New("portFile never got created")
		}
	}
}
