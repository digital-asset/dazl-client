{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";

  # note that the URL is not derived off this version string because the
  # version format is different
  version = "3.3.0-snapshot.20250603.0";

  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v3.3.0-snapshot.20250603.0/canton-open-source-3.3.0-snapshot.20250530.15919.0.v3e7a341c.tar.gz";
    sha256 = "1nhykjizlamj5bihwgxyralcdikjslb4r05n5332sq81cw4xd23w";
  };
  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
