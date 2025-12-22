{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.4.9";

  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "1s6qcvmbp95ydi52y6zc27rw6ij3hzvnaxvk7611k5jyxv54dp60";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
