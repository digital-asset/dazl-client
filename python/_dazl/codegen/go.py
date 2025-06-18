# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
import shutil
from typing import Sequence, TextIO

from .. import dazl_go_module, protoc
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

    go_modules = set[str]()
    for f in response.file:
        name = corrected_name(f.name)
        go_modules.add(name.rpartition("/")[0])

        p = to / name
        p.parent.mkdir(parents=True, exist_ok=True)

        # unfortunately, more than a few files end up generating Go code that does not compile,
        # so they must be fixed afterwards
        write_corrected_content(p, f.content)

    # now write an `import_test.go` that ensures that all generated code is valid and can be compiled

    lines = ['package api_test\n\nimport (\n\t"testing"\n']
    for go_module in sorted(go_modules):
        lines.append(f'\t_ "{dazl_go_module}/go/api/{go_module}"')

    lines.extend([")\n", "func Test(_ *testing.T) {}\n"])

    contents = "\n".join(lines)
    import_test_file = to / "import_test.go"
    import_test_file.write_text(contents)


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
    elif name == "com/digitalasset/canton/time/v30/time_proof.pb.go":
        return "com/digitalasset/canton/protocol/v30/time_proof.pb.go"
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

        else:
            write_content_unchanged(buf, lines)


def write_corrected_content_for_participant_transfer_v0(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        if line == f'\tv01 "{dazl_go_module}/go/api/com/digitalasset/canton/time/v0"':
            pass
        elif "*v01.TimeProof" in line:
            buf.write(line.replace("*v01.TimeProof", "*TimeProof") + "\n")
        else:
            buf.write(line + "\n")


def write_corrected_content_for_participant_transfer_vn(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        if line == f'\tv01 "{dazl_go_module}/go/api/com/digitalasset/canton/time/v0"':
            buf.write(
                f'\tprotocolv0 "{dazl_go_module}/go/api/com/digitalasset/canton/protocol/v0"\n'
            )
        elif "*v01.TimeProof" in line:
            buf.write(line.replace("*v01.TimeProof", "*protocolv0.TimeProof") + "\n")
        else:
            buf.write(line + "\n")


def write_corrected_content_for_timeproof(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        # we move TimeProof into protocol/v0 to avoid circular references,
        # so it doesn't need a reference to its new home package any more
        if line == f'\tv0 "{dazl_go_module}/go/api/com/digitalasset/canton/protocol/v0"':
            pass
        elif "*v0." in line:
            # replace references to the v0 package to local package refs
            buf.write(line.replace("*v0.", "*") + "\n")
        else:
            buf.write(line + "\n")


def write_content_unchanged(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        buf.write(line + "\n")
