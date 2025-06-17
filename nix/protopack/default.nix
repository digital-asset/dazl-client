# Package up all the protobufs that dazl is dependent on in a single derivation.
#
# This is a merge between the canton 2, canton 3, and daml 2 protos.

{
  canton-2,
  canton-3,
  daml-protos-2,
  daml-protos-3,
  gawk,
  protobuf,
  rsync,
  stdenv,
}:

stdenv.mkDerivation rec {
  name = "protopack";
  buildInputs = [ daml-protos-2 daml-protos-3 canton-2 canton-3 gawk protobuf ];
  src = ./.;
  installPhase = ''
    ./copy-daml-2-protos.sh "${daml-protos-2.out}"
    ./copy-daml-3-protos.sh "${daml-protos-3.out}"
    ./copy-canton-2-protos.sh "${canton-2.out}"
    ./copy-canton-3-protos.sh "${canton-3.out}"
    ./build.sh
  '';
}
