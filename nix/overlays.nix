[(self: super: {
  canton-3 = super.callPackage ./canton-3/default.nix {};
  dpm = super.callPackage ./dpm.nix {};
  protopack = super.callPackage ./protopack/default.nix {};
})]
