//go:generate go run internal/damllfpb/update/update.go -- -ast pkg/damlast/ast.go -astdecode pkg/damlast/astdecode.go
package main

import (
	"github.com/digital-asset/dazl/go/cmd"
)

func main() {
	cmd.RunCommandLine()
}
