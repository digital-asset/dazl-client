#!/usr/bin/env python3
import json
from typing import NamedTuple, Optional
from urllib.request import urlopen

from _util import SdkVersion


MINIMUM_SDK_VERSION = SdkVersion(0, 13, 0)


def main():
    sdk_versions = []

    with urlopen('https://api.github.com/repos/digital-asset/daml/releases?per_page=100') as f:
        releases = json.load(f)
        for release in releases:
            if not release['prerelease']:
                version = SdkVersion.parse(release['tag_name'])
                if version is not None and version >= MINIMUM_SDK_VERSION:
                    sdk_versions.append(version)

    for sdk_version in sdk_versions:
        print(sdk_version)


main()
