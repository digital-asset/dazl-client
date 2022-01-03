#!/usr/bin/env pipenv run python3
# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).absolute().parent.parent


def main():
    parser = ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    all_files = get_all_files()
    copyright_notice = extract_copyright_notice()

    if args.dry_run:
        print("Copyright header:")
        for notice_line in copyright_notice:
            print("    " + notice_line)
        print("")
        print("Files to modify:")
        for py_file in all_files:
            print("    " + str(py_file))
    else:
        for py_file in all_files:
            modify_header(py_file, copyright_notice)
            print(f"Updated {py_file}")


def get_all_files() -> "Sequence[Path]":
    python_files = [*ROOT.glob("**/*.py"), *ROOT.glob("**/*.yaml")]
    files = []
    for py_file in python_files:
        if (
            ".tmp" not in str(py_file)
            and "_gen" not in str(py_file)
            and "scripts" not in str(py_file)
        ):
            files.append(py_file)
    return files


def modify_header(path: Path, header_string: "Sequence[str]") -> None:
    """
    Modify the copyright header of the specified file.
    """
    with path.open("r") as f:
        lines = f.readlines()

    rewrite = []
    found_header = False
    for line in lines:
        if found_header:
            rewrite.append(line.rstrip() + "\n")
        elif line.startswith("#!"):
            rewrite.append(line.rstrip() + "\n")
        elif line.startswith("#"):
            continue
        else:
            if not found_header:
                found_header = True
                rewrite.extend(map(lambda x: x + "\n", header_string))
            rewrite.append(line.rstrip() + "\n")

    with path.open("w") as f:
        f.writelines(rewrite)


def extract_copyright_notice() -> "Sequence[str]":
    """
    Silly little method to extract the copyright header directly from this file.
    """
    comments = []
    with open(__file__, "r") as f:
        for line in f:
            if line.startswith("#!"):
                continue
            if line.startswith("#"):
                comments.append(line.rstrip())
            else:
                return comments

    raise ValueError("Couldn't find a copyright header in this file!")


if __name__ == "__main__":
    main()
