{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.7.0-snapshot.20261023.20808.0.vf4863aea";

  src = builtins.fetchurl {
    url =
      if builtins.match ".*-snapshot.*" version != null
      # snapshots from unstable GAR maven repo
      then "https://europe-maven.pkg.dev/da-images/public-maven-unstable/com/digitalasset/canton/canton-api/${version}/canton-api-${version}.tar.gz"
      # stable versions from github OSS canton releases
      else "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";

    sha256 = "sha256:1kgi4672zmvi8sxv3kf09kwpqpkpn99aysbh1g2vfza4i7isynvj";
  };

  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
