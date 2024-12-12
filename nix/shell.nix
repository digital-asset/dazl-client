{ pkgs, ci }:
let
  requiredPackages = with pkgs; ([
    # these packages are required both in CI and for local development
    jq
    go
    openjdk
    poetry
    protoc-gen-go
    protoc-gen-go-grpc
    python39
    python310
    python311
    python312
    yamlfmt

  ] ++ (if ci then [
    # these packages should only be installed on CI

  ] else [
    # these packages are only installed on developer machines locally
  ]));

in
pkgs.mkShell {
  GOROOT = "";
  GOPATH = "";
  packages = requiredPackages;
}
