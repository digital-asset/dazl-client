# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
DAML-LF Archive parsing
-----------------------

Functions for creating :class:`Archive` and :class:`Package` instances.

:func:`parse_archive` can be used to take an arbitrary byte payload from the Package Service and
convert it to an :class:`Archive`; an :class:`Archive` contains the package and its modules, which
in turn contain templates, data types, and values.
"""

import sys
import time
from typing import Optional

from .._gen.com.daml.daml_lf_1_15.daml_lf_pb2 import ArchivePayload
from .daml_lf_1 import Archive, PackageRef
from .pb_parse import ProtobufParser

__all__ = ["parse_archive", "parse_archive_payload"]


def parse_archive(package_id: "PackageRef", archive_bytes: bytes) -> "Archive":
    """
    Convert ``bytes`` into an :class:`Archive`.
    """
    archive_pb = parse_archive_payload(package_id, archive_bytes)

    parser = ProtobufParser(package_id)
    package = parser.parse_Package(archive_pb.daml_lf_1)

    return Archive(package_id, package)


def parse_archive_payload(
    package_id: "Optional[PackageRef]", archive_bytes: bytes
) -> "ArchivePayload":
    """
    Convert ``bytes`` into a :class:`G.ArchivePayload`.

    Note that this function will temporarily increase Python's recursion limit to handle cases where
    parsing a DAML-LF archive requires deeper recursion limits.
    """
    # noinspection PyPackageRequirements
    from google.protobuf.message import DecodeError

    from .. import LOG

    current_time = time.time()

    prev_recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(5000)
    archive_payload = ArchivePayload()
    try:
        archive_payload.ParseFromString(archive_bytes)
    except DecodeError:
        # noinspection PyPackageRequirements
        from google.protobuf.internal import api_implementation  # type: ignore

        if api_implementation.Type() == "cpp":
            LOG.error("Failed to decode metadata. This may be due to bugs in the native Protobuf")
            LOG.error("implementation as exposed through Python, so setting an environment")
            LOG.error("variable to force a non-native implementation may help work around this")
            LOG.error("problem:")
            LOG.error("    export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python")
        raise
    finally:
        sys.setrecursionlimit(prev_recursion_limit)

    final_time = time.time()
    total_millis = (final_time - current_time) * 1000
    if package_id is None:
        LOG.info("Parsed %s bytes of metadata in %0.2f ms.", len(archive_bytes), total_millis)
    else:
        LOG.info(
            "Parsed %s bytes of metadata (package ID %r) in %0.2f ms.",
            len(archive_bytes),
            package_id,
            total_millis,
        )

    return archive_payload
