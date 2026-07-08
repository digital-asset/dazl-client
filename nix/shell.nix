{ pkgs }: pkgs.mkShell {
  packages = with pkgs; ([
    # these packages are required both in CI and for local development
    canton-3
    daml-2
    dpm
    glibcLocales
    jq
    go
    openjdk
    poetry
    protobuf
    protoc-gen-go
    protoc-gen-go-grpc
    python310
    python311
    python312
    python313
    ruff
    yamlfmt
  ]);

  GOROOT = "";
  GOPATH = "";

  PROTOPACK_DIR = "${pkgs.protopack.out}";

  # required to get grpclib working for Python
  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";

  # MacOS doesn't seem to like this for some reason
  ${if pkgs.stdenv.isLinux then "LOCALE_ARCHIVE" else null} = "${pkgs.glibcLocales}/lib/locale/locale-archive";
}
