#!/usr/bin/env python3
# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Fetch Protobuf definitions for DAML-LF, the Ledger API, and other protobuf files required
for Ledger API clients.
"""

import shutil
from pathlib import Path
from typing import BinaryIO, Optional, Union

ROOT = Path(__file__).absolute().parent.parent

DAML_SDK_VERSION = '100.13.40'
DAML_SDK_BASE_URL = 'https://digitalassetsdk.bintray.com/DigitalAssetSDK'
GOOGLE_APIS_BASE_URL = 'https://raw.githubusercontent.com/googleapis/googleapis/master'

DAML_LF_TGZ = 'daml-lf-dev-archive-proto.tar.gz'
LEDGER_API_TGZ = 'ledger-api-protos.tar.gz'
GOOGLE_RPC_STATUS_PROTO = 'google-rpc-status.proto'


fetch_urls = {
    DAML_LF_TGZ: f'{DAML_SDK_BASE_URL}/com/digitalasset/daml-lf-dev-archive-proto/{DAML_SDK_VERSION}/daml-lf-dev-archive-proto-{DAML_SDK_VERSION}.tar.gz',
    LEDGER_API_TGZ: f'{DAML_SDK_BASE_URL}/com/digitalasset/ledger-api-protos/{DAML_SDK_VERSION}/ledger-api-protos-{DAML_SDK_VERSION}.tar.gz',
    GOOGLE_RPC_STATUS_PROTO: f'{GOOGLE_APIS_BASE_URL}/google/rpc/status.proto',
}


def main():
    import tarfile
    import zipfile

    cache_dir = ROOT / '.cache'
    cache_dir.mkdir(parents=True, exist_ok=True)

    download_dir = cache_dir / 'download'
    protos_dir = cache_dir / 'protos'

    for file_path, url in fetch_urls.items():
        download_url(url, download_dir / file_path)

    if protos_dir.exists():
        shutil.rmtree(protos_dir)

    copy(src=download_dir / GOOGLE_RPC_STATUS_PROTO,
         dest=protos_dir / 'google/rpc/status.proto')

    with tarfile.open(download_dir / LEDGER_API_TGZ) as tar:
        for tarinfo in tar:
            if tarinfo.isfile():
                p = remainder(tarinfo.name, './grpc-definitions/')
                if p is not None:
                    with tar.extractfile(tarinfo) as from_:
                        copy(src=from_, dest=protos_dir / p)

    with tarfile.open(download_dir / DAML_LF_TGZ) as tar:
        for tarinfo in tar:
            if tarinfo.isfile():
                p = remainder(tarinfo.name, './com/digitalasset/daml_lf_dev/')
                if p is not None:
                    with tar.extractfile(tarinfo) as from_:
                        copy(src=from_, dest=protos_dir / 'com' / 'digitalasset' / 'daml_lf_dev' / p)


def copy(src: 'Union[BinaryIO, Path]', dest: 'Path') -> 'Path':
    dest.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(src, Path):
        shutil.copyfile(str(src), str(dest))
    else:
        with dest.open('wb') as dest_file:
            shutil.copyfileobj(src, dest_file)
    return dest


def download_url(url: str, path: 'Path') -> 'Path':
    from urllib.request import urlopen

    if path.exists():
        return path

    with urlopen(url) as response:
         path.parent.mkdir(parents=True, exist_ok=True)
         with path.open('wb') as f:
             shutil.copyfileobj(response, f)
    return path


def remainder(s: str, prefix: str) -> 'Optional[str]':
    if s.startswith(prefix):
        return s[len(prefix):]
    else:
        return None


if __name__ == '__main__':
    main()
