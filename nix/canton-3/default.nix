{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";

  version = "3.5.1-rc3";

  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "0bcmmxrh3fs63hqp543s42l8lb1wwiidsp2a5gbvq4dyg7imzibr";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
