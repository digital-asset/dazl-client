{
  stdenv,
  unzip,
}:

stdenv.mkDerivation rec {
  pname = "daml-protos";
  version = "2.10.1";
  buildInputs = [ unzip ];
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v2.10.1/protobufs-2.10.1.zip";
    sha256 = "1a3a91jvp8sqqfdsv2c3fmlpq8xxhgl848sxdcnadj8x48zs7vsg";
  };
  dontUnpack = true;
  buildPhase = ''
    unzip $src
  '';

  # the only protobufs from the Daml 2.x package that we care about are the latest Daml-LF
  installPhase = ''
    mkdir -p "$out/com/daml/ledger/api"
    cp -R "protos-2.10.1/com/daml/daml_lf_1_17" "$out/com/daml/"
    cp -R "protos-2.10.1/com/daml/ledger/api/v1" "$out/com/daml/ledger/api"
  '';
}
