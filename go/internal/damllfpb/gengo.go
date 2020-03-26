package damllfpb

import (
	"bytes"
	"fmt"
	"go/format"
	"path"
	"runtime"
	"text/template"
)

func RenderGoModel(root *Root) string {
	_, filename, _, ok := runtime.Caller(0)
	if !ok {
		panic("Where are we?!?!?!")
	}
	//var builder strings.Builder
	pattern := path.Dir(filename) + "/*.go.tmpl"

	t, err := template.ParseGlob(pattern)
	if err != nil {
		panic(err)
	}

	var buf bytes.Buffer
	err = t.ExecuteTemplate(&buf, "ast.go.tmpl", root)
	if err != nil {
		panic(err)
	}

	formattedCode, err := format.Source(buf.Bytes())
	if err != nil {
		fmt.Println(err)
		return buf.String()
	}

	return string(formattedCode)
}

func RenderGoParser(root *Root) string {
	_, filename, _, ok := runtime.Caller(0)
	if !ok {
		panic("Where are we?!?!?!")
	}
	//var builder strings.Builder
	pattern := path.Dir(filename) + "/*.go.tmpl"

	t, err := template.ParseGlob(pattern)
	if err != nil {
		panic(err)
	}

	var buf bytes.Buffer
	err = t.ExecuteTemplate(&buf, "astdecode.go.tmpl", root)
	if err != nil {
		panic(err)
	}

	formattedCode, err := format.Source(buf.Bytes())
	if err != nil {
		fmt.Println(err)
		return buf.String()
	}

	return string(formattedCode)

}
