import pkg_resources
import logging
import shutil
from . import LOG
from .config import CONFIG
from pathlib import Path
from grpc_tools import protoc



def grpc_gen():
    pyraw_dir = CONFIG.directories.pyraw
    if pyraw_dir.exists():
        shutil.rmtree(pyraw_dir)
    pyraw_dir.mkdir(parents=True, exist_ok=True)

    generate_raw_bindings(CONFIG.directories.protos, pyraw_dir, True)
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
