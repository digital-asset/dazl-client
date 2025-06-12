{ pkgs, ci }:
let
  requiredPackages = with pkgs; ([
    # these packages are required both in CI and for local development
    glibcLocales
    jq
    go
    openjdk
    poetry
    protoc-gen-go
    protoc-gen-go-grpc
    python310
    python311
    python312
    python313
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

  # required to get grpclib working for Python
  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";

  # MacOS doesn't seem to like this for some reason
  ${if pkgs.stdenv.isLinux then "LOCALE_ARCHIVE" else null} = "${pkgs.glibcLocales}/lib/locale/locale-archive";

  packages = requiredPackages;
}
