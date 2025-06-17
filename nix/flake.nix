{
  inputs = {
    nixpkgs.url = "nixpkgs/7db94fc7a741a6f6b621073fd8f49345595251a8";
    flake-utils.url = "github:numtide/flake-utils/11707dc2f618dd54ca8739b309ec4fc024de578b";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs { inherit system; overlays = import ./overlays.nix; };
        in
        {
          devShells.default = import ./shell.nix { inherit pkgs ; ci = false; };
          devShells.ci = import ./shell.nix { inherit pkgs ; ci = true; };
        }
      );
}
