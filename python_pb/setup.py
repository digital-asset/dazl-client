#!/usr/bin/env python3
# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import shutil
import tarfile
import zipfile

from distutils.cmd import Command
from pathlib import Path
from setuptools import setup
from setuptools.command.build_py import build_py
from typing import BinaryIO, Optional, Union
from urllib.request import urlopen


# Version of this library. Generally the same as the SDK version.
VERSION = '100.13.10'

# The DAML SDK version to download artifacts from.
DAML_SDK_VERSION = VERSION


ROOT = Path(__file__).absolute().parent

DAML_SDK_BASE_URL = 'https://digitalassetsdk.bintray.com/DigitalAssetSDK'
GOOGLE_APIS_BASE_URL = 'https://raw.githubusercontent.com/googleapis/googleapis/master'

DAML_LF_JAR = f'daml-lf-archive-{DAML_SDK_VERSION}.jar'
LEDGER_API_TGZ = f'ledger-api-protos-{DAML_SDK_VERSION}.tar.gz'
GOOGLE_RPC_STATUS_PROTO = 'google-rpc-status.proto'


fetch_urls = {
    DAML_LF_JAR: f'{DAML_SDK_BASE_URL}/com/digitalasset/daml-lf-archive/{DAML_SDK_VERSION}/daml-lf-archive-{DAML_SDK_VERSION}.jar',
    LEDGER_API_TGZ: f'{DAML_SDK_BASE_URL}/com/digitalasset/ledger-api-protos/{DAML_SDK_VERSION}/ledger-api-protos-{DAML_SDK_VERSION}.tar.gz',
    GOOGLE_RPC_STATUS_PROTO: f'{GOOGLE_APIS_BASE_URL}/google/rpc/status.proto',
}



def fetch():
    """
    Fetch Protobuf definitions for DAML-LF, the Ledger API, and other protobuf files required
    for Ledger API clients.
    """
    cache_dir = ROOT / '.cache'
    cache_dir.mkdir(parents=True, exist_ok=True)

    download_dir = cache_dir / 'download'
    protos_dir = cache_dir / 'protos' / DAML_SDK_VERSION

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

    with zipfile.ZipFile(download_dir / DAML_LF_JAR) as jar:
        for name in jar.namelist():
            p = remainder(name, 'daml-lf/archive/')
            if p is not None:
                with jar.open(name) as from_:
                    copy(src=from_, dest=protos_dir / p)


def copy(src: 'Union[BinaryIO, Path]', dest: 'Path') -> 'Path':
    dest.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(src, Path):
        shutil.copyfile(str(src), str(dest))
    else:
        with dest.open('wb') as dest_file:
            shutil.copyfileobj(src, dest_file)
    return dest


def download_url(url: str, path: 'Path') -> 'Path':
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



class FetchCommand(Command):
    description = 'fetch Protobuf dependencies'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        fetch()


class GenerateSourceCommand(Command):
    description = 'fetch Protobuf dependencies'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.run_command('fetch')



class BuildPyCommand(build_py):
  """Custom build command."""

  def run(self):
    self.run_command('generate_py')
    build_py.run(self)


setup(
    name='dazl-pb',
    version=VERSION,
    python_requires='>=3.6',
    author='Digital Asset (Switzerland) GmbH',
    author_email='support@digitalasset.com',
    cmdclass={
        'fetch': FetchCommand,
        'generate_py': GenerateSourceCommand,
        'build_py': BuildPyCommand,
    },
    install_requires=[
        'grpcio>=1.20.1',
        'protobuf>=3.8.0',
    ])

