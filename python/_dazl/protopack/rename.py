# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the logic for how Protobuf files are renamed.
"""

from __future__ import annotations

from typing import Collection, Mapping, Optional, Set


def canton_proto_files(zip_file_names: Collection[str]) -> Mapping[str, str]:
    """
    Return paths to Canton protobuf/gRPC files that are interesting for code generation.
    The key is the "short" file path (starting with com/digitalasset) and the value is
    the full file path as it exists in the Canton .zip file distribution.
    """
    file_names = {}
    for name in zip_file_names:
        components = name.split("/")
        short_name = "/".join(name.split("/")[3:])

        if short_name == "com/digitalasset/canton/topology/admin/v0/topology_ext.proto":
            # this file has a different package name from its file location for historical
            # reasons, but leaving it like this breaks Python codegen because it has
            # an expectation that these lines match
            file_names["com/digitalasset/canton/protocol/v0/topology_ext.proto"] = name

        elif short_name == "com/digitalasset/canton/time/admin/v0/domain_time_service.proto":
            file_names["com/digitalasset/canton/domain/api/v0/domain_time_service.proto"] = name

        elif (
            components[1] == "protobuf"
            and components[-1].endswith(".proto")
            and not name.endswith("package.proto")
        ):
            # grab everything in the */protobuf directory that is a Protobuf file except
            # for the package.proto files, since those are just configuration for
            # Scala code generation, and that doesn't apply here
            file_names[short_name] = name
    return file_names


def daml_proto_files(zip_file_names: Collection[str]) -> Mapping[str, str]:
    """
    Return paths to Daml protobuf/gRPC files that are interesting for code generation.
    The key is the "short" file path (starting with com/daml) and the value is
    the full file path as it exists in the Canton .zip file distribution.

    :param zip_file_names:
        The names of files inside the Daml protobuf distribution.
    """
    file_names = {}

    daml_lf_dir = detect_daml_lf_dir(zip_file_names)
    if daml_lf_dir is None:
        print(zip_file_names)
        raise ValueError("could not detect daml_lf_dir")
    for name in zip_file_names:
        short_name = "/".join(name.split("/")[1:])

        if short_name.startswith("com/daml/ledger/api/v1/") and short_name.endswith(".proto"):
            # Ledger API protos
            file_names[short_name] = name
        elif short_name.startswith(daml_lf_dir) and short_name.endswith(".proto"):
            # Daml-LF protos
            file_names[short_name] = name

    return file_names


def detect_daml_lf_dir(paths: Collection[str]) -> Optional[str]:
    """
    Find the biggest Daml-LF v1 version in the set of file names from a Protobuf archive, and return
    the path that contains the associated files (with a trailing slash).

    This code will need to be revisited with Daml-LF 2 is stable.

    :param paths: The paths in a Protobuf zipfile to examine.
    :return: The root directory of a target Daml-LF protobuf version, stripped of a prefix.

    >>> detect_daml_lf_dir([
    ...    "protos-1.15.0/com/daml/daml_lf_1_10/something.proto",
    ...    "protos-1.15.0/com/daml/daml_lf_1_9/something.proto",
    ...    "protos-1.15.0/com/daml/daml_lf_dev/something.proto",
    ...    "protos-1.15.0/com/daml/daml_lf_1_what/something.proto",
    ... ])
    'com/daml/daml_lf_1_10/'
    """
    daml_lf_prefix = "com/daml/daml_lf_1_"

    minor_versions = set()  # type: Set[int]
    for p in paths:
        _, _, truncated_path = p.partition("/")

        if truncated_path.startswith(daml_lf_prefix):
            version_str, _, _ = truncated_path[len(daml_lf_prefix) :].partition("/")
            try:
                minor_versions.add(int(version_str))
            except ValueError:
                # skip over unrecognized directory names
                pass
    if minor_versions:
        return f"{daml_lf_prefix}{max(minor_versions)}/"
    else:
        return None
