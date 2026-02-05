{ pkgs ? import <nixpkgs> {} }:

let
  dpmPath = "europe-docker.pkg.dev/da-images/public/components/dpm";
  dpmVersion = "1.0.9";
  dpmRef = "${dpmPath}:${dpmVersion}";

  dpmHashes = {
    "x86_64-linux" = "sha256-owwatMwR9W8FCx3GjirYuPpY/fEcQj1izi0Ao4ebGoQ=";
    "aarch64-linux" = "sha256-4k1kgv6uWEFJPmNatYS0iu/er6TdTlIFEXedG9zK/Rs=";
    "x86_64-darwin" = "sha256-qr52rFVtw2dyDJSvj4vj45DLu8U8Q/citQ2+4cULcOA=";
    "aarch64-darwin" = "sha256-hVZZet+JoAI04W/6lWh0i6ovwWsNJ59GPTGONjZBlAY=";
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
