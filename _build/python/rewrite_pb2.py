# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import re
import sys
from pathlib import Path


FROM = re.compile(r'from ([\w.]+) import (\w+) as (\w+)')


def main():
    rewrite_file(sys.argv[1], sys.argv[2], sys.argv[3])


def rewrite_file(input_file, root_path, copyright_file) -> str:
    if not input_file.startswith(root_path):
        raise Exception()

    current_module = input_file[len(root_path) + 1:]
    current_module = current_module.rpartition('/')[0].replace('/', '.')
    with Path(copyright_file).open('r', encoding='utf-8') as f:
        for line in f.readlines():
            print('# ' + line.rstrip())
        
    with Path(input_file).open('r', encoding='utf-8') as f:
        for line in f.readlines():
            print(rewrite_import(current_module, line).rstrip())


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
            return f'from . import {identifier_name} as {local_name}'

    return line


if __name__ == '__main__':
    main()
