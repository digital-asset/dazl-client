#!/usr/bin/env bash
set -euo pipefail

protos="$1/protobuf"

# copy the lib directory as-is (do NOT apply our awk-isms), as these
# are mostly the standard Google libraries
protos_lib="${protos}/lib"
for proto in $(find "${protos_lib}" -type f -name '*.proto' ! \( -name 'package.proto' -or -name 'scalapb.proto' \) )
do
  target_proto_base="${proto#$protos_lib/}"
  target_proto="${out}/lib/${target_proto_base}"

  mkdir -p "$(dirname "${target_proto}")"
  cp "${proto}" "${target_proto}"
done

# for the canton protos, some light modifications to add go package
# declarations and remove references to scalapb
for api in admin-api community ledger-api participant synchronizer
do
  protos_api="${protos}/${api}"
  for proto in $(find "${protos_api}" -type f -name '*.proto' ! -name 'package.proto')
  do
    target_proto_base="${proto#$protos_api/}"
    target_proto="${out}/protos/${target_proto_base}"

    mkdir -p "$(dirname "${target_proto}")"
    awk -f patches.awk "${proto}" > "${target_proto}"
  done
done
