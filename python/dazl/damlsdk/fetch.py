# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities for fetching DAML SDK components.
"""

import platform
import tarfile
from dataclasses import dataclass
from pathlib import Path
from shutil import rmtree
from tempfile import TemporaryDirectory
from typing import Union, Tuple
from urllib.parse import urlparse
from urllib.request import urlretrieve


from .artifacts import load_artifacts, get_artifact_url, parse_component_identifier

from semver import VersionInfo

from .. import LOG


@dataclass(frozen=True)
class FetchResult:
    path: Path
    url: str
    downloaded: bool


def sdk_component_path(component: str) -> Tuple[str, Path]:
    name, version = parse_component_identifier(component, use_default_version=True)
    return name, ensure_sdk_component(name, version).path


def ensure_sdk_component(
        component: str,
        version: Union[None, str, VersionInfo],
        force: bool = False) -> FetchResult:
    """
    Ensures the existence of an SDK component. This may download the component first.
    """
    artifacts = load_artifacts()
    target_platform = 'osx' if platform.system() == 'Darwin' else 'linux'

    artifact_loc = artifacts.artifacts[component]
    if version is not None and isinstance(version, str):
        version = VersionInfo.parse(version)
    elif not isinstance(version, VersionInfo):
        version = artifact_loc.default_version
        if version is None:
            raise ValueError(f'the component {component!r} does not have a default version defined')

    url = get_artifact_url(artifacts.root_url, artifact_loc, version, platform=target_platform)

    installation_dir = Path.home() / '.da' / 'packages' / component / str(version)
    if installation_dir.exists():
        # if the top-level directory already exists, assume we already downloaded it
        if not force:
            return FetchResult(installation_dir, url, False)
    else:
        installation_dir.parent.mkdir(parents=True, exist_ok=True)

    if artifact_loc.packaging in ('tar.gz', 'tgz'):
        extract_sdk_tgz(url, installation_dir, force=force)
    elif artifact_loc.packaging is None or artifact_loc.packaging == 'jar':
        download_package(url, installation_dir)
    else:
        LOG.warning('The packaging type %s does not have a defined mechanism for handling',
                    artifact_loc.packaging)
        download_package(url, installation_dir)

    return FetchResult(installation_dir, url, True)


def extract_sdk_tgz(url: str, target_directory: Path, force: bool = False):
    if not force and target_directory.exists():
        raise RuntimeError(f'the directory already exists: {target_directory}')

    temp_dir = Path.home() / '.da' / 'tmp'
    if not temp_dir.exists():
        temp_dir.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory(dir=temp_dir) as td:
        tempdir = Path(td)

        download_package(url, tempdir)
        pkg = next(tempdir.iterdir())

        untarred = Path(tempdir) / "extract"
        with tarfile.open(pkg) as tar:
            tar.extractall(untarred)

        rmtree(target_directory, ignore_errors=True)
        next(untarred.iterdir()).rename(target_directory)

        # a little Mojave hack to work around bad packaging of Haskell components
        bad_lib = target_directory / "lib" / "libSystem.B.dylib"
        if bad_lib.exists():
            bad_lib.unlink()


def download_package(url: str, output_directory: Path) -> Path:
    if not output_directory.exists():
        output_directory.mkdir(parents=True)

    p = urlparse(url)
    filename = p.path.rpartition('/')[-1]
    path = output_directory / filename

    try:
        urlretrieve(url, path)
    except:
        LOG.exception('Failed to download %s', url)
        raise

    return path
