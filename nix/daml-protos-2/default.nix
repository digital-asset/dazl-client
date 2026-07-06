{
  stdenv,
  unzip,
}:

stdenv.mkDerivation rec {
  pname = "daml-protos";
  version = "2.10.4";
  buildInputs = [ unzip ];
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/protobufs-${version}.zip";
    sha256 = "01nw3i6y1hpn656k8l4k6751v052zyba7wp6f1wvkpx000h5hxh4";
  };
  dontUnpack = true;
  buildPhase = ''
    unzip $src
  '';

  # the only protobufs from the Daml 2.x package that we care about are Ledger API v1
  # Daml-LF 1 is still present in the Daml 3.x line, and in a way that integrates better
  # with Daml-LF 2
  installPhase = ''
    mkdir -p "$out/com/daml/ledger/api"
    cp -R "protos-${version}/com/daml/ledger/api/v1" "$out/com/daml/ledger/api"
  '';
}
