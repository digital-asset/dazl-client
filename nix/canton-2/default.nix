{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "2.10.3";
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "0qv2n5rg60378n3ygig5ijzwn8jwkkqya1d2xns6apacr3qxp8ks";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
