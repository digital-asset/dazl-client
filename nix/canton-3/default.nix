{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";

  # note that the URL is not derived off this version string because the
  # version format is different
  version = "3.4.10";

  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/canton-open-source-${version}.tar.gz";
    sha256 = "02rm44kv31dhanv2hj56y8hw5r2hwp4n82n0bjj7izi6hbhg2xcs";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
