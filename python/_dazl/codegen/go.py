# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
import shutil
from typing import Sequence, TextIO

from .. import protoc
from .go_header import HEADER

__all__ = ["go_files"]


def go_files(from_: Path, to: Path) -> None:
    response = protoc.run(
        from_,
        plugins=["go", "go-grpc"],
        options=["--go_opt=paths=source_relative", "--go-grpc_opt=paths=source_relative"],
    )
    if to.exists():
        shutil.rmtree(to)

    for f in response.file:
        name = corrected_name(f.name)

        p = to / name
        p.parent.mkdir(parents=True, exist_ok=True)

        # unfortunately, more than a few files end up generating Go code that does not compile,
        # so they must be fixed afterwards
        write_corrected_content(p, f.content)


def corrected_name(name: str) -> str:
    # these files cause circular import errors if we leave them where they are, so they have to be moved
    if name == "com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.pb.go":
        return "com/digitalasset/canton/domain/admin/v0sequencerinitializationservice/sequencer_initialization_service.pb.go"
    elif (
        name
        == "com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service_grpc.pb.go"
    ):
        return "com/digitalasset/canton/domain/admin/v0sequencerinitializationservice/sequencer_initialization_service_grpc.pb.go"
    elif name == "com/digitalasset/canton/time/v0/time_proof.pb.go":
        return "com/digitalasset/canton/protocol/v0/time_proof.pb.go"
    else:
        return name


def write_corrected_content(path: Path, content: str) -> None:
    lines = content.splitlines()
    if content.startswith("// Copyright (c)"):
        # the Go generated code extracts its copyright information from the Protobuf header, but it
        # differs slightly from the copyright string that is used in the dazl codebase. Remove the
        # copyright header if it exists, and we'll add it back later
        lines = lines[2:]

    with path.open("w") as buf:
        buf.write(HEADER)

        if path.name == "participant_transfer.pb.go":
            if "/protocol/v0/" in str(path):
                write_corrected_content_for_participant_transfer_v0(buf, lines)
            else:
                write_corrected_content_for_participant_transfer_vn(buf, lines)

        elif path.name == "time_proof.pb.go":
            write_corrected_content_for_timeproof(buf, lines)

        elif "/daml_lf_1_15/" in str(path):
            write_corrected_content_for_damllf(buf, lines)

        else:
            write_content_unchanged(buf, lines)


def write_corrected_content_for_damllf(buf: TextIO, lines: Sequence[str]) -> None:
    # the Daml-LF protobufs unfortunately mix Protobuf package names in the same directory,
    # and that causes the Go Protobuf compiler to spit out nonsense. Fix the package names
    # so that they are consistent, drop a meaningless broken import, and drop an unnecessary
    # qualified reference

    for line in lines:
        if line == "package daml_lf_15":
            buf.write("package daml_lf_1_15\n")
        elif (
            line
            == '\tdaml_lf_15 "github.com/digital-asset/dazl-client/v7/go/api/com/daml/daml_lf_15"'
        ):
            pass
        elif "*daml_lf_15.Package" in line:
            buf.write(line.replace("*daml_lf_15.Package", "*Package") + "\n")

        else:
            # nothing unusual about this line, so just write it as is
            buf.write(line + "\n")


def write_corrected_content_for_participant_transfer_v0(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        if (
            line
            == '\tv01 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/time/v0"'
        ):
            pass
        elif "*v01.TimeProof" in line:
            buf.write(line.replace("*v01.TimeProof", "*TimeProof") + "\n")
        else:
            buf.write(line + "\n")


def write_corrected_content_for_participant_transfer_vn(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        if (
            line
            == '\tv01 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/time/v0"'
        ):
            buf.write(
                '\tprotocolv0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v0"\n'
            )
        elif "*v01.TimeProof" in line:
            buf.write(line.replace("*v01.TimeProof", "*protocolv0.TimeProof") + "\n")
        else:
            buf.write(line + "\n")


def write_corrected_content_for_timeproof(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        # we move TimeProof into protocol/v0 to avoid circular references,
        # so it doesn't need a reference to its new home package any more
        if (
            line
            == '\tv0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v0"'
        ):
            pass
        elif "*v0." in line:
            # replace references to the v0 package to local package refs
            buf.write(line.replace("*v0.", "*") + "\n")
        else:
            buf.write(line + "\n")


def write_content_unchanged(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        buf.write(line + "\n")
