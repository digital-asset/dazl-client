{ pkgs ? import <nixpkgs> {} }:

let
  dpmVersion = "1.0.16";

  dpmHashes = {
    "x86_64-linux" = "sha256:0x4qfnzb4bk0c5l46vbr4hlcsjkhvhm5q7yybkq9kryhnga22x1q";
    "aarch64-linux" = "sha256:0kmvn4vxbcl411g14fx5b60kasbj5ay2zr3y1bjzf2izf09502vb";
    "x86_64-darwin" = "sha256:0bwy68n6qrh54hra1sbk4pif5aijxm945x92m5816vl06qayscyw";
    "aarch64-darwin" = "sha256:18lawi0m2kmcaw792lni6y7kkm61s4lz0p0amy6jla4dnb2dmvxq";
  };
  dpmHash = dpmHashes.${pkgs.system} or (throw "Unsupported system: ${pkgs.system}");

  ociPlatforms = {
    "x86_64-linux" = "linux-amd64";
    "aarch64-linux" = "linux-arm64";
    "x86_64-darwin" = "darwin-amd64";
    "aarch64-darwin" = "darwin-arm64";
  };
  ociPlatform = ociPlatforms.${pkgs.system} or (throw "Unsupported system: ${pkgs.system}");
in
pkgs.stdenv.mkDerivation {
  name = "dpm-gh";

 src = builtins.fetchurl {
    url = "https://github.com/digital-asset/dpm/releases/download/${dpmVersion}/dpm-${dpmVersion}-${ociPlatform}.tar.gz";
    sha256 = "${dpmHash}";
  };

  sourceRoot = ".";
  installPhase = ''
    mkdir -p $out/bin
    cp -r * "$out/bin"
  '';
}
