#!/usr/bin/env bash
set -euox pipefail

protos="$1/protobuf"

protos_community="${protos}/community"
for proto in $(find "${protos_community}" -type f -name '*.proto' ! -name 'package.proto')
do
  target_proto_base="${proto#$protos_community/}"
  target_proto="${out}/protos/${target_proto_base}"

  # some of these protobuf from the Canton 2 distribution need to be renamed in order to prevent
  # Python protoc codegen from breaking; the package name and the directory name do not match for these
  case "${target_proto_base}" in
    com/digitalasset/canton/topology/admin/v0/topology_ext.proto)
      target_proto="${out}/protos/com/digitalasset/canton/protocol/v0/topology_ext.proto"
      ;;
    com/digitalasset/canton/time/admin/v0/domain_time_service.proto)
      target_proto="${out}/protos/com/digitalasset/canton/domain/api/v0/domain_time_service.proto"
      ;;
    com/digitalasset/canton/protocol/v0/versioned-google-rpc-status.proto)
      target_proto="${out}/protos/com/digitalasset/canton/protocol/v0/versioned_google_rpc_status.proto"
      ;;
  esac

  mkdir -p "$(dirname "${target_proto}")"
  awk -f patches-canton-2.awk "${proto}" > "${target_proto}"
done

for api in domain participant
do
  protos_api="${protos}/${api}"
  for proto in $(find "${protos_api}" -type f -name '*.proto' ! -name 'package.proto')
  do
    target_proto_base="${proto#$protos_api/}"
    target_proto="${out}/protos/${target_proto_base}"
    mkdir -p "$(dirname "${target_proto}")"
    awk -f patches-canton-2.awk "${proto}" > "${target_proto}"
  done
done
