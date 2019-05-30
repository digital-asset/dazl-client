# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import yaml
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Tuple

from semver import VersionInfo

from ..util.prim_types import to_boolean


@dataclass(frozen=True)
class ArtifactRepository:
    root_url: str
    artifacts: 'Dict[str, ArtifactLocation]'


@dataclass(frozen=True)
class ArtifactLocation:
    group_id: str
    artifact: str
    default_version: VersionInfo
    packaging: Optional[str] = None
    native: bool = False


def load_artifacts() -> 'ArtifactRepository':
    artifacts_yaml_file = Path(__file__).parent / 'artifacts.yaml'
    with artifacts_yaml_file.open() as f:
        d = yaml.load(f, yaml.SafeLoader)

    root_url = d.get('rootUrl')
    artifacts = d.get('artifacts')

    return ArtifactRepository(root_url, {key: _parse_artifact_dict(value)
                                         for key, value in artifacts.items()})


def _parse_artifact_dict(d: 'Mapping[str, Any]') -> 'ArtifactLocation':
    group_id = d.get('groupId')
    artifact = d.get('artifact')
    if group_id is None or artifact is None:
        raise ValueError('"groupId" and "artifact" must always be specified')

    native = d.get('native')
    if native is None:
        native = False
    else:
        try:
            native = to_boolean(native)
        except ValueError:
            raise ValueError(f'"native" must be a boolean (got {native!r} instead)')

    return ArtifactLocation(
        group_id, artifact, VersionInfo.parse(d.get('defaultVersion')),
        d.get('packaging'), native)


def parse_component_identifier(name: str, use_default_version: bool = False) \
        -> 'Tuple[str, Optional[VersionInfo]]':
    """
    Turn a string that looks like ``component`` or ``component:version`` into a tuple of component
    name and/or semver, optionally filling in the version value from the default taken from the
    manifest.

    :param name:
        The string that identifies the component, in the form ``component[:version]``.
    :param use_default_version:
        ``True`` to look in dazl's artifact manifest for a suggested version if none is supplied;
        otherwise, ``False`` to simply return ``None`` for version information.
    :return:
        A tuple of component name and optional version.
    :raise ValueError:
        ``name`` is not a valid component string

    >>> parse_component_identifier('sandbox')
    ('sandbox', None)
    >>> parse_component_identifier('sandbox:6.0.0')
    ('sandbox', VersionInfo(major=6, minor=0, patch=0, prerelease=None, build=None))
    """
    if name is None:
        raise ValueError('name is required')

    component, _, version = name.partition(':')
    if not component:
        raise ValueError('component name must be specified')

    parsed_version = VersionInfo.parse(version) if version else None
    if parsed_version is None:
        if use_default_version:
            parsed_version = load_artifacts().artifacts[component].default_version

    return component, parsed_version


def get_default_version(name: str) -> 'Optional[VersionInfo]':
    return load_artifacts().artifacts[name].default_version


def get_artifact_url(
        root_url: str,
        location: 'ArtifactLocation',
        version: 'Optional[VersionInfo]' = None,
        platform: 'Optional[str]' = None) -> str:
    requested_version = version or location.default_version
    if root_url.endswith('/'):
        root_url = root_url[:-1]

    group = location.group_id.replace('.', '/')
    ext = location.packaging or 'jar'
    if location.native:
        if platform is None:
            raise ValueError('platform is required for native binaries')
        file_name = f'{location.artifact}-{requested_version}-{platform}.{ext}'
    else:
        file_name = f'{location.artifact}-{requested_version}.{ext}'

    return f'{root_url}/{group}/{location.artifact}/{requested_version}/{file_name}'
