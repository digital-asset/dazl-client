#!/usr/bin/env python3
# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import logging
from os.path import basename
from pathlib import Path
from typing import Mapping, Sequence
from zipfile import ZipFile
from io import TextIOWrapper


Manifest = Mapping[str, Sequence[str]]


def main():
    from argparse import ArgumentParser

    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser(description='Unpack the DAML SDK protobuf package.')
    parser.add_argument('--input', '-i', required=True, action='append')
    parser.add_argument('--output', '-o', required=True)
    parser.add_argument('--output-manifest', '-m')
    args = parser.parse_args()

    logging.info('Unpacker processing these files:')
    for p in args.input:
        logging.info('    %s', p)

    unpacker = Unpacker([Path(p) for p in args.input], Path(args.output))
    manifest = unpacker.run()

    if args.output_manifest:
        with open(args.output_manifest, 'w') as f:
            json.dump(manifest, f, indent='  ')


class Unpacker:
    def __init__(self, inputs: 'Sequence[Path]', output: 'Path'):
        self.inputs = inputs
        self.output = output

    def run(self) -> 'Manifest':
        manifest = {}

        for input_path in self.inputs:
            if input_path.suffix == '.zip':
                manifest.update(self._process_zip(input_path))
            elif input_path.suffix == '.proto':
                manifest.update(self._process_proto(input_path))
            else:
                raise ValueError(f"don't know how to process {input_path.path}")
        
        return manifest
    
    def _process_zip(self, path: 'Path') -> 'Manifest':
        proto_packages = {}  # type: Manifest
        with ZipFile(path) as z:
            logging.info('Procesing zip file: %s', path)
            for zi in z.infolist():
                logging.info('    Processing file: %s', zi.filename)
                if is_valid_proto(zi.filename) and not zi.is_dir():
                    with z.open(zi) as f:
                        with TextIOWrapper(f) as text_buf:
                            contents = text_buf.read()
                    try:
                        proto_packages.update(self._process_proto_contents(basename(zi.filename), contents))
                    except ValueError:
                        logging.exception('Could not process %s', zi.filename)
        return proto_packages

    def _process_proto(self, path: 'Path') -> 'Manifest':
        try:
            return self._process_proto_contents(path.name, path.read_text())
        except ValueError:
            logging.exception('Could not process %s', path)
        return {}

    def _process_proto_contents(self, short_name: str, contents: str) -> 'Manifest':
        lines = contents.splitlines()
        if not lines:
            return {}

        # look for a package directive
        package_lines = [line for line in lines if line.startswith('package ')]
        if not package_lines:
            raise ValueError('file is missing a package directive')

        package = package_lines[0].rstrip(';')[8:]

        is_grpc = any(line.startswith('service') for line in lines)

        rel_file = dest_dir(package) + '/' + short_name
        
        out_file = self.output / rel_file
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(contents)

        return { rel_file.rpartition('.')[0]: ['pb', 'grpc'] if is_grpc else ['pb'] }


def dest_dir(package: str) -> str:
    """
    Modify the package directive in a Protobuf file to put it in a more "expected" place.
    """
    if package in ('daml_lf_dev', 'daml_lf_1'):
        return 'com/daml/daml_lf_dev'
    else:
        return package.replace('.', '/')


def is_valid_proto(path: 'Path') -> bool:
    # We prefer DAML-LF 1.dev because dev is always a strict superset of
    # the latest 1.x version, but also allows us to build and test support for
    # experimental features before they are released.
    if path is None:
        return False

    p = str(path)
    return p.endswith('.proto') and \
        '/daml_lf_1_6/' not in p and \
        '/daml_lf_1_7/' not in p and \
        '/daml_lf_1_8/' not in p and \
        '/daml_lf_1_11/' not in p
    

if __name__ == '__main__':
    main()
