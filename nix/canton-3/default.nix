{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.7.0-snapshot.20261014.20770.0.v0fd13468";

  src = builtins.fetchurl {
    url =
      if builtins.match ".*-snapshot.*" version != null
      # snapshots from unstable GAR maven repo
      then "https://europe-maven.pkg.dev/da-images/public-maven-unstable/com/digitalasset/canton/canton-api/${version}/canton-api-${version}.tar.gz"
      # stable versions from github OSS canton releases
      else "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";

    sha256 = "sha256:076mbm6gm0c2gxr10q90g9byigadwc2wrw2pmi6jrf69cgr66v2l";
  };

  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
