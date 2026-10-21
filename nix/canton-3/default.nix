{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.7.0-snapshot.20261020.20787.0.v43fb7df8";

  src = builtins.fetchurl {
    url =
      if builtins.match ".*-snapshot.*" version != null
      # snapshots from unstable GAR maven repo
      then "https://europe-maven.pkg.dev/da-images/public-maven-unstable/com/digitalasset/canton/canton-api/${version}/canton-api-${version}.tar.gz"
      # stable versions from github OSS canton releases
      else "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";

    sha256 = "sha256:1dg1y0mz4j3fpds9jbvk66198jchxy5j79zxxc99pm67nbsy972x";
  };

  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
