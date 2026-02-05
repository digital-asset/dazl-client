{
  stdenv,
  unzip,
}:

stdenv.mkDerivation rec {
  pname = "daml-protos";
  version = "2.10.3";
  buildInputs = [ unzip ];
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/protobufs-${version}.zip";
    sha256 = "1s4k9ra09ziwghlfkzgnxx32xxnvhsir2hvxcnny0n7hyxj0g29v";
  };
  dontUnpack = true;
  buildPhase = ''
    unzip $src
  '';

  # the only protobufs from the Daml 2.x package that we care about are the latest Daml-LF
  installPhase = ''
    mkdir -p "$out/com/daml/ledger/api"
    cp -R "protos-2.10.3/com/daml/daml_lf_1_17" "$out/com/daml/"
    cp -R "protos-2.10.3/com/daml/ledger/api/v1" "$out/com/daml/ledger/api"
  '';
}
