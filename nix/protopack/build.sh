#!/usr/bin/env bash
set -euo pipefail

cd "$out/protos"
protoc --descriptor_set_out="$out/protos.pb" -I../lib -I. $(find . -name '*.proto')
