{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";

  version = "3.5.1-rc5";

  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "sha256-Ou9Zso0kYILTR1FzfyAT0jijT6OnbD7JDLbfS5VwsTY=";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
