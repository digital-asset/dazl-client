{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.7.3-snapshot.20261111.20904.0.vbe797d9d";

  src = builtins.fetchurl {
    url =
      if builtins.match ".*-snapshot.*" version != null
      # snapshots from unstable GAR maven repo
      then "https://europe-maven.pkg.dev/da-images/public-maven-unstable/com/digitalasset/canton/canton-api/${version}/canton-api-${version}.tar.gz"
      # stable versions from github OSS canton releases
      else "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";

    sha256 = "sha256:1npi8dqan2mkd1m414cjjymybns13azl0xldrmz2331gzg96x07s";
  };

  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
