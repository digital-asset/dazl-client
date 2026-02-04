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

  # the only protobufs from the Daml 2.x package that we care about are Ledger API v1
  # Daml-LF 1 is still present in the Daml 3.x line, and in a way that integrates better
  # with Daml-LF 2
  installPhase = ''
    mkdir -p "$out/com/daml/ledger/api"
    cp -R "protos-${version}/com/daml/ledger/api/v1" "$out/com/daml/ledger/api"
  '';
}
