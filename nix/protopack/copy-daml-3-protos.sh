#!/usr/bin/env bash
set -euo pipefail

protos="$1"

for proto in $(find "${protos}" -type f -name '*.proto')
do
  # Skip daml_lf1.proto - we use daml_lf_1_17 from daml-protos-2 instead
  if [[ "${proto}" == *"daml_lf1.proto" ]]; then
    continue
  fi

  target_proto_base="${proto#$protos/}"
  target_proto="${out}/protos/${target_proto_base}"

  mkdir -p "$(dirname "${target_proto}")"
  awk -f patches-daml-3.awk "${proto}" > "${target_proto}"
done
