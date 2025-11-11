# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from . import daml_lf_1 as lf
from ..util.version import SdkVersion
from .parse_factory.pb_parse_base import ProtobufParserBase
from .parse_factory.pb_v1 import ProtobufParser117
from .parse_factory.pb_v2 import ProtobufParser21

__all__ = ["ProtobufParserFactory", "UnsupportedVersionError"]


class UnsupportedVersionError(Exception):
    """Raised when an unsupported DAML-LF version is encountered."""

    pass


class ProtobufParserFactory:
    """
    Factory for creating DAML-LF protobuf parsers based on version.

    Supports:
    - DAML-LF 1.x or DAML-LF 2.x (via ProtobufParser117)
    - DAML-LF 3.x (via ProtobufParser21)

    The factory uses lazy loading to avoid circular imports and unnecessary
    module loading overhead.
    """

    @classmethod
    def create_parser(
        cls, package_id: lf.PackageRef, sdk_version: Optional[str]
    ) -> ProtobufParserBase:
        """
        Create a parser for the specified DAML-LF version.

        Args:
            package_id: The package ID being parsed
            version: Version string (e.g., "1.17", "2.1", "3.3)

        Returns:
            Version-specific parser instance

        Raises:
            UnsupportedVersionError: If version is not supported
        """

        version = SdkVersion.parse(sdk_version)
        if version is None:
            raise UnsupportedVersionError(f"Unsupported DAML-LF version: {sdk_version}")

        if version.major == 1 or version.major == 0 or version.major == 2:
            return ProtobufParser117(package_id)
        elif version.major == 3:
            return ProtobufParser21(package_id)

        # default to old parser for unknown versions
        return ProtobufParser117(package_id)
