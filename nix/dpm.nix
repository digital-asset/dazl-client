{ pkgs ? import <nixpkgs> {} }:

let
  dpmPath = "europe-docker.pkg.dev/da-images/public/components/dpm";
  dpmVersion = "1.0.6";
  dpmRef = "${dpmPath}:${dpmVersion}";

  dpmHashes = {
    "x86_64-linux" = "sha256-WFly1i2QRKDV5OIAOaguBrlyTO9zb5MBvZdZy3aZqwo=";
    "aarch64-linux" = "sha256-jEYFr7q1EXa1NUF25af39E+ZUqoWLvufIGDdrCnVi60=";
    "x86_64-darwin" = "sha256-nUmd3isAUmoehdeqSiak7StA8R2s+tHIvbWI/6PEg1w=";
    "aarch64-darwin" = "sha256-WCk/5SYrf9/GSibhqNq24JdGXODLrlp+hlFfn+d45kQ=";
  };
  dpmHash = dpmHashes.${pkgs.system} or (throw "Unsupported system: ${pkgs.system}");

  ociPlatforms = {
    "x86_64-linux" = "linux/amd64";
    "aarch64-linux" = "linux/arm64";
    "x86_64-darwin" = "darwin/amd64";
    "aarch64-darwin" = "darwin/arm64";
  };
  ociPlatform = ociPlatforms.${pkgs.system} or (throw "Unsupported system: ${pkgs.system}");
in
pkgs.stdenv.mkDerivation {
  pname = "dpm";
  version = dpmVersion;

  src = pkgs.stdenv.mkDerivation {
    name = "dpm-pull-${dpmRef}.${ociPlatform}";

    nativeBuildInputs = [ pkgs.oras pkgs.cacert ];

    buildCommand = ''
      set -e
      echo "Pulling dpm component from ${dpmRef} for platform ${ociPlatform}"
      oras pull --platform ${ociPlatform} -o $out ${dpmRef}
    '';
    outputHashMode = "recursive";
    outputHashAlgo = "sha256";
    outputHash = dpmHash;
  };

  installPhase = ''
    mkdir -p $out/bin
    install -Dm755 $src/dpm $out/bin/dpm
  '';
}
