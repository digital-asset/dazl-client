{
  stdenv,
  unzip,
}:

stdenv.mkDerivation rec {
  pname = "daml-protos";
  version = "3.3";
  buildInputs = [ unzip ];
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v3.3.0-snapshot.20250603.0/protobufs-3.3.0-snapshot.20250528.13806.0.v3cd439fb.zip";
    sha256 = "1rln4v128f4444fng31361yx280b2sx2y20ic7sncdp9hvn01i1c";
  };
  dontUnpack = true;
  buildPhase = ''
    unzip $src
  '';

  # the only protobufs from the Daml 3.x package that we care about are the latest Daml-LF
  installPhase = ''
    mkdir -p "$out/com/daml/ledger/api"
    cp -R "protos-3.3.0-snapshot.20250528.13806.0.v3cd439fb/com/daml/daml_lf_2_1" "$out/com/daml/"
  '';
}
