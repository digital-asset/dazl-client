#!/usr/bin/env .venv/bin/python3
# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import re
import shutil
from pathlib import Path
from typing import List

import pkg_resources
from grpc_tools import protoc


def setup_logger():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    root.addHandler(handler)


setup_logger()
LOG = logging.getLogger('dazl/generate.py')


ROOT = Path(__file__).absolute().parent
FROM = re.compile(r'from ([\w.]+) import (\w+) as (\w+)')


def main() -> None:
    generate_proto_bindings(ROOT / '.cache' / 'protos' / '100.13.10')


def generate_proto_bindings(protos_path: Path):
    COPYRIGHT_NOTICE = extract_copyright_notice()

    output_directory = ROOT / ".tmp" / "gen"
    final_output_dir = ROOT / "dazl" / "_gen"

    try:
        shutil.rmtree(str(output_directory))
    except FileNotFoundError:
        pass
    output_directory.mkdir(parents=True)

    generate_raw_bindings(protos_path, ROOT / '.cache' / 'py-raw', True)
    return

    (output_directory / "1").mkdir()
    (output_directory / "1" / "__init__.py").touch()

    for src_file in sorted(list((output_directory / "0").rglob('**/*.py'))):
        rel = src_file.relative_to(output_directory / "0")
        dest_file = output_directory / "1" / rel

        LOG.info("Copying %s to %s", src_file, dest_file)
        # make sure all parent directories (and Python modules) exist
        ensure_module_path(dest_file)

        current_module = str(rel.parent).replace('/', '.')

        with src_file.open(mode='r', encoding='utf-8') as src:
            src_lines = src.readlines()

        if len(src_lines) >= 5:
            with dest_file.open(mode='w', encoding='utf-8') as dest:
                dest.writelines(COPYRIGHT_NOTICE)

                for line in src_lines:
                    # rewrite cross-service imports to be relative imports instead so that we can avoid
                    # polluting the root module namespace
                    dest.write(rewrite_import(current_module, line))

    shutil.rmtree(str(final_output_dir))
    (output_directory / "1").rename(final_output_dir)


def rewrite_import(parent_module: str, line: str) -> str:
    result = FROM.match(line)
    if result:
        module_name = result.group(1)
        identifier_name = result.group(2)
        local_name = result.group(3)
        if module_name.startswith('google.'):
            # don't rewrite Google imports; simply do nothing
            return line
        if module_name == parent_module:
            return f'from . import {identifier_name} as {local_name}\n'

    return line


def ensure_module_path(path: Path) -> None:
    if path.parent != path:
        ensure_module_path(path.parent)

    if path.exists():
        return
    if path.parent.exists():
        return

    path.parent.mkdir()
    (path.parent / "__init__.py").touch()


def generate_raw_bindings(input_directory: Path, output_directory: Path, grpc: bool) -> int:
    """
    Create .py files that correspond to all of the .proto files (recursively) listed in the
    specified directory.

    :param input_directory: Directory to read .proto files from.
    :param output_directory: Directory to write .py files to.
    :param grpc: True to generate ``grpc`` bindings as well as Protobuf bindings.
    """
    proto_files = list(input_directory.rglob('**/*.proto')) + list(input_directory.rglob('**/*.grpc'))
    output_directory.mkdir(parents=True, exist_ok=True)

    protoc_args = [
        # this is sys.argv[0]; note that the value can literally be anything but we set it to
        # something useful for debugging purposes only
        'pipenv run python3 -m grpc_tools.protoc',
        f'-I{input_directory}/',
        f'--python_out={output_directory}']
    if grpc:
        protoc_args.append(f'--grpc_python_out={output_directory}')
    protoc_args.extend(map(str, proto_files))

    if LOG.isEnabledFor(logging.INFO):
        # output the command we're going to run in a way that is compatible with command-line usage
        LOG.info('Running protoc with these args:')
        last_arg = len(protoc_args) - 1
        for i, arg in enumerate(protoc_args):
            if i == 0:
                LOG.info('    %s \\', arg)
            elif i == last_arg:
                LOG.info('        %s', arg)
            else:
                LOG.info('        %s \\', arg)

    # for some reason, this is injected _outside_ of the implementation of `protoc.main`
    protoc_args.append(f"-I{pkg_resources.resource_filename('grpc_tools', '_proto')}")

    return protoc.main(protoc_args)


def extract_copyright_notice() -> List[str]:
    """
    Silly little method to extract the copyright header directly from this file.
    """
    comments = []
    with open(__file__, 'r') as f:
        comments = f.readlines()[1:3]
    return comments


if __name__ == '__main__':
    main()
