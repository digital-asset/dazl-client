# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
from typing import Final, Sequence, Union

__all__ = ["daml_sdk_versions", "known_version_1", "known_version_2", "known_versions"]


known_version_1: Final = "1.18.3"
known_version_2: Final = "2.9.6"
known_versions: Final = (known_version_1, known_version_2)


def daml_sdk_versions(allowed_versions: Union[None, str, Sequence[str]] = None) -> Sequence[str]:
    if allowed_versions is None:
        allowed_versions = known_versions
    elif isinstance(allowed_versions, str):
        allowed_versions = (allowed_versions,) if allowed_versions in known_versions else ()
    else:
        allowed_versions = tuple(v for v in known_versions if v in allowed_versions)

    env_sdk_version = os.getenv("DAML_SDK_VERSION")
    if env_sdk_version:
        # return a single version--the one that we are configured to run with
        return (env_sdk_version,) if env_sdk_version in allowed_versions else ()
    else:
        # return all the versions that we might care about
        return allowed_versions
