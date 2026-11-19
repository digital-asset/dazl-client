# Package up all the protobufs that dazl is dependent on in a single derivation.
#
# This is a merge between the canton 2, canton 3, and daml 2 protos.

{
  canton-3,
  gawk,
  protobuf,
  rsync,
  stdenv,
}:

stdenv.mkDerivation rec {
  name = "protopack";
  buildInputs = [ canton-3 gawk protobuf ];
  src = ./.;
  installPhase = ''
    ./copy-canton-3-protos.sh "${canton-3.out}"
    ./build.sh
  '';
}
