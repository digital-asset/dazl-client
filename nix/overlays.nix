[(self: super: {
  canton-2 = super.callPackage ./canton-2/default.nix {};
  canton-3 = super.callPackage ./canton-3/default.nix {};
  daml-protos-2 = super.callPackage ./daml-protos-2/default.nix {};
  daml-protos-3 = super.callPackage ./daml-protos-3/default.nix {};
  protopack = super.callPackage ./protopack/default.nix {};
  splice-openapi = super.callPackage ./splice-openapi/default.nix {};
})]
