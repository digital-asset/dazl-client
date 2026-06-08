{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";

  version = "3.5.2";

  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "sha256-k1AKhDxS6XB2Hpo8LZl2VHlOq8FxzaIJkc7t4W6Zi0Q=";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
