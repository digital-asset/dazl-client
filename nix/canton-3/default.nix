{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.7.0-snapshot.20261028.20828.0.v5a0b7c60";

  src = builtins.fetchurl {
    url =
      if builtins.match ".*-snapshot.*" version != null
      # snapshots from unstable GAR maven repo
      then "https://europe-maven.pkg.dev/da-images/public-maven-unstable/com/digitalasset/canton/canton-api/${version}/canton-api-${version}.tar.gz"
      # stable versions from github OSS canton releases
      else "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";

    sha256 = "sha256:1j0da5ms4sb6kz4jnbw6dc9gaq38bmlrhax2p97gdiwa9bq10lkq";
  };

  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
