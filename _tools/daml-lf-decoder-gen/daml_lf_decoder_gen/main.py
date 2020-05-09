from pathlib import Path

import pkg_resources
from grpc_tools import protoc
from google.protobuf.descriptor_pb2 import FileDescriptorSet

from daml_lf_decoder_gen.decode_fds import decode_fds
from daml_lf_decoder_gen.render_json import render_json
from daml_lf_decoder_gen.render_py import render_py, render_pyi


def main():
    root = Path(__file__).parent.parent.parent.parent / '.cache/protos'
    ledger_api_fds_path = Path(__file__).parent.parent.parent.parent / '.cache/fds.pb'
    generate_fd_proto(root, ledger_api_fds_path)

    ledger_api_fds = FileDescriptorSet()
    ledger_api_fds.ParseFromString(ledger_api_fds_path.read_bytes())
    package = decode_fds(ledger_api_fds)

    import sys
    renderer = sys.argv[1]
    if renderer == 'py-model':
        print(render_py(package))
    elif renderer == 'py-typing':
        print(render_pyi(package))
    elif renderer == 'go':
        print(render_py(package))
    elif renderer == 'json':
        print(render_json(package))
    else:
        raise ValueError(f'unknown renderer: {renderer}')


def generate_fd_proto(input_directory: Path, output_file_descriptor: Path):
    proto_files = list(input_directory.rglob('com/daml/daml_lf_dev/*.proto'))
    output_file_descriptor.parent.mkdir(parents=True, exist_ok=True)

    protoc_args = [
        # this is sys.argv[0]; note that the value can literally be anything but we set it to
        # something useful for debugging purposes only
        'python3 -m grpc_tools.protoc',
        f'-I{input_directory}/',
        f'-o{output_file_descriptor}',
        '--include_source_info'
    ]
    protoc_args.extend(map(str, proto_files))

    # for some reason, this is injected _outside_ of the implementation of `protoc.main`
    protoc_args.append(f"-I{pkg_resources.resource_filename('grpc_tools', '_proto')}")
    return protoc.main(protoc_args)
