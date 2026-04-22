{ pkgs ? import <nixpkgs> {} }:

let
  dpmPath = "europe-docker.pkg.dev/da-images/public/components/dpm";
  dpmVersion = "1.0.12";
  dpmRef = "${dpmPath}:${dpmVersion}";

  dpmHashes = {
    "x86_64-linux" = "sha256-iR/kQy0u/aoLd/8AZCg6Dpf2YAaxlzepffoyzu5bqnQ=";
    "aarch64-linux" = "sha256-iSekabTFHp2ulP1soJbnP036pZOV4OJ3Za+UGfZDmLI=";
    "x86_64-darwin" = "sha256-jAFLS4Qr+ewkEgqgrtYm8+D+ur0htMzSso/jPIAFWpE=";
    "aarch64-darwin" = "sha256-m9I67SSjvuBMYXixY5HNpSD0bAACg7xpHbVJglVZfxw=";
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
