//+build ignore
package main

import (
	"flag"
	"github.com/digital-asset/dazl/go/internal/damllfpb"
	"io/ioutil"
)

func main() {
	var astPath, astDecodePath string
	flag.StringVar(&astPath, "ast", "", "Path to write an ast.go")
	flag.StringVar(&astDecodePath, "astdecode", "", "Path to write an astdecode.go")
	flag.Parse()

	// TODO: Why isn't flag parsing working here?
	if astPath == "" {
		astPath = flag.Arg(1)
	}
	if astDecodePath == "" {
		astDecodePath = flag.Arg(3)
	}

	print("Writing ast.go to: " + astPath + "\n")
	print("Writing astdecode.go to: " + astDecodePath + "\n")

	root, err := damllfpb.BuildRoot()
	if err != nil {
		panic(err)
	}

	err = ioutil.WriteFile(astPath, []byte(damllfpb.RenderGoModel(root)), 0644)
	if err != nil {
		panic(err)
	}

	err = ioutil.WriteFile(astDecodePath, []byte(damllfpb.RenderGoParser(root)), 0644)
	if err != nil {
		panic(err)
	}
}
