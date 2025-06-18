#!/usr/bin/env bash
set -euo pipefail

protos="$1"

for proto in $(find "${protos}" -type f -name '*.proto')
do
  target_proto_base="${proto#$protos/}"
  target_proto="${out}/protos/${target_proto_base}"

  mkdir -p "$(dirname "${target_proto}")"
  awk -f patches-daml-2.awk "${proto}" > "${target_proto}"
done
