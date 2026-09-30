{ stdenv }:

stdenv.mkDerivation rec {
  pname = "canton-open-source";
  version = "3.5.19";

  src = builtins.fetchurl {
    url =
      if builtins.match ".*-snapshot.*" version != null
      # snapshots from unstable GAR maven repo
      then "https://europe-maven.pkg.dev/da-images/public-maven-unstable/com/digitalasset/canton/canton-api/${version}/canton-api-${version}.tar.gz"
      # stable versions from github OSS canton releases
      else "https://github.com/digital-asset/canton/releases/download/v${version}/canton-open-source-${version}.tar.gz";

    sha256 = "sha256:154ll0mysllv63xrxil453vrv0wljvgl16spr0k14sqysjfqyyfm";
  };

  installPhase = ''
    mkdir -p "$out"
    cp -r * "$out"
  '';
}