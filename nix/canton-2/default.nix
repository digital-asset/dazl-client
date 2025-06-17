{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "2.10.1";
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "1zny3nav0syh21sy5s8c4c8hvhwv23djy19r3xpjn2w88kacglqq";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
