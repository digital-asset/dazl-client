#!/usr/bin/env bash
set -euxo pipefail

dazl_whl=$(buck build //sdk/templates/dazl --show-full-output | cut -d ' ' -f 2)
dazl_it=$HOME/Repositories/da/sdk/templates/dazl/_template

(
    cd ubuntu18
    docker build . -t digitalasset/dazl-ubuntu18-test
    docker run \
        -v$dazl_whl:/tmp/dazl-0-py3-none-any.whl \
        -v$HOME/.da:/root/.da \
        -v$dazl_it:/root/test \
        digitalasset/dazl-ubuntu18-test
)
