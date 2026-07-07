{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "2.10.4";
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "0l107vmhsp7c5gmzq9ds6sacg9944qrs9glj51wwhff1pjjbwfmd";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
