#!/usr/bin/env python3
# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import logging
import os
from os.path import basename
from pathlib import Path
from typing import Mapping, Sequence, Union, Dict
from zipfile import ZipFile
from io import TextIOWrapper


Manifest = Mapping[str, Sequence[str]]


def main():
    from argparse import ArgumentParser

    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser(description='Unpack the Daml Connect Protobuf package.')
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
            else:
                raise ValueError(f"don't know how to process {input_path}")
        
        return manifest
    
    def _process_zip(self, path: 'Path') -> 'Manifest':
        proto_packages = {}  # type: Dict[str, Sequence[str]]
        with ZipFile(path) as z:
            logging.info('Processing zip file: %s', path)
            for zi in z.infolist():
                logging.info('    Processing file: %s', zi.filename)
                if is_valid_proto(zi.filename) and not zi.is_dir():
                    # strip off the top-level directory name; we don't need it
                    _, _, path = zi.filename.partition('/')
                    with z.open(zi) as f:
                        with TextIOWrapper(f) as text_buf:
                            contents = text_buf.read()
                    try:
                        proto_packages.update(self._process_proto_contents(path, contents))
                    except ValueError:
                        logging.exception('Could not process %s', zi.filename)
        return proto_packages

    def _process_proto_contents(self, rel_file: str, contents: str) -> 'Manifest':
        lines = contents.splitlines()
        if not lines:
            return {}

        is_grpc = any(line.startswith('service') for line in lines)

        out_file = self.output / rel_file
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(contents)

        return { rel_file.rpartition('.')[0]: ['pb', 'grpc'] if is_grpc else ['pb'] }


def is_valid_proto(path: 'Union[str, Path]') -> bool:
    # We prefer DAML-LF 1.dev because dev is always a strict superset of
    # the latest 1.x version, but also allows us to build and test support for
    # experimental features before they are released.
    if path is None:
        return False

    p = os.fspath(path)
    return p.endswith('.proto') and \
        '/daml_lf_1_6/' not in p and \
        '/daml_lf_1_7/' not in p and \
        '/daml_lf_1_8/' not in p and \
        '/daml_lf_1_11/' not in p and \
        '/daml_lf_1_12/' not in p and \
        '/daml_lf_1_13/' not in p and \
        '/daml_lf_dev/' not in p


if __name__ == '__main__':
    main()
