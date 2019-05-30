# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from dataclasses import dataclass
from typing import Optional, Sequence

from .. import LOG
from .fetch import sdk_component_path
from ..util.process import ProcessContext


@dataclass
class PackageOptions:
    """
    Options that control how DAML packages are constructed.
    """
    files: 'Sequence[str]'
    output_path: str
    extra_args: 'Sequence[str]'


def package(options: 'PackageOptions', component: 'Optional[str]' = None) -> 'ProcessContext':
    name, path = sdk_component_path(component or 'damlc')

    if name != 'damlc':
        raise ValueError(f'Unknown packaging component: {component}')

    LOG.info('Using %s to create a DAR package...', name)
    args = [path / 'da-hs-damlc-app', *_damlc_package_options(options)]
    return ProcessContext(args, logger=logging.getLogger('damlc'))


def _damlc_package_options(options: 'PackageOptions') -> 'Sequence[str]':
    if options.extra_args:
        return ['package', *options.files, *options.extra_args, 'package-name', '-o', options.output_path]
    else:
        return ['package', *options.files, 'package-name', '-o', options.output_path]


