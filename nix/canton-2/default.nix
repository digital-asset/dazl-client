{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "2.10.6";
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "sha256:0y6b1r70m0mcs809md97fwn9xn0v228a98ff3w38zyrkbmxckvq6";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
