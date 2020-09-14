import sys
from pathlib import Path


# We intentionally exclude daml_lf_0.proto because its sole Protobuf message, 'Package', conflicts
# with a much more valuable daml_lf_1.proto 'Package' message; as a result, we'll also drop
# the ``ArchivePayload`` message's ability to understand DAML-LF v0 files (of which no modern DAML
# compiler produces anyway).
SUBSTITUTE_LINES = {
    'import "com/daml/daml_lf_dev/daml_lf_0.proto";': '',
    '    daml_lf_0.Package daml_lf_0 = 1;': '    // daml_lf_0.Package daml_lf_0 = 1;'
}


def main():
    rewrite_file(sys.argv[1], sys.argv[2], sys.argv[3])


def rewrite_file(input_file, go_mod, root_path) -> str:
    go_module = get_go_module(go_mod)

    current_module = input_file[len(root_path) + 1:]
    go_package, _, _ = current_module.rpartition('/')

    with Path(input_file).open() as f:
        lines = [line.rstrip() for line in f]
    
    # If the proto file already has a Go package declared, assume that we don't need to generate
    # anything for it; this will break down if the DAML SDK Protobuf files ever include a Go
    # package, but if that happens, we may not need to have this code generator here.
    if any(line.startswith('option go_package') for line in lines):
        # just print out the entire file exactly as is and bail
        for line in lines:
            print(line)
        return
    
    # We couldn't find a go_package, so assume we need to generate Go files.
    did_write_option = False
    for line in lines:
        if line.startswith('option ') and not did_write_option:
            print(f'option go_package = "{go_module}/pkg/generated/{go_package}";')
            did_write_option = True
        else:
            print(SUBSTITUTE_LINES.get(line, line))


def get_go_module(go_mod):
    with Path(go_mod).open() as f:
        for line in f:
            if line.startswith('module '):
                return line[7:].strip()


if __name__ == '__main__':
    main()
