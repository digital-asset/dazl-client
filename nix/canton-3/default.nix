{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.7.0-snapshot.20260929.20584.0.vbb57304b";

  src = builtins.fetchurl {
    url =
      if builtins.match ".*-snapshot.*" version != null
      # snapshots from unstable GAR maven repo
      then "https://europe-maven.pkg.dev/da-images/public-maven-unstable/com/digitalasset/canton/canton-api/${version}/canton-api-${version}.tar.gz"
      # stable versions from github OSS canton releases
      else "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";

    sha256 = "sha256:0r9vgfxd5vhybmm2lai8zv3z20rbxv6rfvz13h80s9wmhv9cmw07";
  };

  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}
