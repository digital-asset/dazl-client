#!/usr/bin/env python3
import json
import logging
from os import PathLike, fspath
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Optional, Sequence
from zipfile import ZipFile
from io import TextIOWrapper


Manifest = Mapping[str, Sequence[str]]


def main():
    from argparse import ArgumentParser

    logging.basicConfig()

    parser = ArgumentParser(description='Unpack the DAML SDK protobuf package.')
    parser.add_argument('--input', '-i', required=True, action='append')
    parser.add_argument('--output', '-o', required=True)
    parser.add_argument('--output-manifest', '-m')
    args = parser.parse_args()

    unpacker = Unpacker([PathSpec.parse(p) for p in args.input], Path(args.output))
    manifest = unpacker.run()

    if args.output_manifest:
        with open(args.output_manifest, 'w') as f:
            json.dump(manifest, f, indent='  ')


@dataclass(frozen=True)
class PathSpec:
    """
    An individual input file to unpack.

    Attributes:
        path:
            Path to the file to read data from. Can be a .zip file or a
            .proto file.
        relative_root:
            For .zip files, the name of a folder in the zip file to treat as the
            Protobuf root; for other files, the directory on the file system to
            be used as a root for ``path``.
    """

    @classmethod
    def parse(cls, s: str):
        p, _, r = s.partition(':')
        return cls(Path(p), r)

    path: Path
    relative_root: 'Optional[str]' = None

    def relative(self, p: PathLike) -> Optional[str]:
        """
        Evaluate the file path, and return the part of the path contained in this
        directory, but only if the file exists in the relative root.
        """
        f = fspath(p)
        print(f, self.relative_root)
        if f is not None and self.relative_root is not None and f.startswith(self.relative_root):
            return f[len(self.relative_root):].lstrip('/')
        else:
            return None
    
    def as_proto_record(self) -> 'ProtoRecord':
        return ProtoRecord()


@dataclass(frozen=True)
class ProtoRecord:
    name: str
    contents: str


@dataclass(frozen=True)
class Unpacker:
    inputs: 'Sequence[PathSpec]'
    output: 'Path'

    def run(self) -> 'Manifest':
        manifest = {}

        for input_path_spec in self.inputs:
            if input_path_spec.path.suffix == '.zip':
                manifest.update(self._process_zip(input_path_spec))
            elif input_path_spec.path.suffix == '.proto':
                manifest.update(self._process_proto(input_path_spec))
            else:
                raise ValueError(
                    f"don't know how to process {input_path_spec.path}")
        
        return manifest
    
    def _process_zip(self, zip_file_spec: 'PathSpec') -> 'Manifest':
        proto_packages = {}  # type: Manifest
        with ZipFile(zip_file_spec.path) as z:
            for zi in z.infolist():
                path = zip_file_spec.relative(zi.filename)
                print(zi.filename, path)
                if path is not None and not zi.is_dir():
                    with z.open(zi) as f:
                        with TextIOWrapper(f) as text_buf:
                            contents = text_buf.read()
                    proto_packages.update(self._process_proto(PathSpec(path, None), contents=contents))
        return proto_packages

    def _process_proto(self, proto_file_spec: 'PathSpec', contents: 'Optional[str]' = None) -> 'Manifest':
        logging.info(proto_file_spec)
        if contents is None:
            contents = proto_file_spec.path.read_text()

        name = proto_file_spec.relative(proto_file_spec.path) if proto_file_spec.relative_root is not None else proto_file_spec.path
        if name is None:
            print(proto_file_spec)
            return {}

        is_grpc = any(line.startswith('service') for line in contents.splitlines())
        
        out_file = self.output / name
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(contents)

        return { name.rpartition('.')[0]: ['pb', 'grpc'] if is_grpc else ['pb'] }
    

if __name__ == '__main__':
    main()
