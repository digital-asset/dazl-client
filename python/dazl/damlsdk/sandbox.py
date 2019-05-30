# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities for starting up a local instance of the Ledger Sandbox,
either through the Sandbox or one local to the build tree of the project.
"""

import logging
from contextlib import ExitStack
from pathlib import Path
from typing import Collection, Sequence, Optional, Type, Union, Tuple, ContextManager

from dataclasses import dataclass

from .. import LOG
from .fetch import sdk_component_path
from ..model.core import DazlError
from ..model.ledger import TimeModel, StaticTimeModel, RealTimeModel
from ..model.network import SSLSettings
from ..util.process import ProcessContext, ProcessWatcher


@dataclass(frozen=True)
class SandboxOptions:
    """
    Parameters that indicate how a sandbox is to be started.
    """
    files: 'Sequence[Union[str, Path]]'
    port: 'int'
    extra_args: 'Sequence[str]'


def sandbox(daml_path: 'Union[str, Path, Collection[str], Collection[Path]]',
            port: 'Optional[int]' = None,
            backend: 'Optional[str]' = None,
            damlc: 'Optional[str]' = None,
            time_model_type: 'Type[TimeModel]' = StaticTimeModel,
            ssl_settings: 'Optional[SSLSettings]' = None,
            extra_args: 'Optional[Sequence[str]]' = None,
            damlc_extra_args: 'Optional[Sequence[str]]' = None) -> ProcessWatcher:
    """
    Run an instance of the Sandbox.

    :param daml_path:
        The path to the DAML file or DAR file to open, or a list of files.
    :param port:
        The port to bind the server to, or ``None`` to pick a port at random and use it.
    :param backend:
        ``None`` to use the default backend (``'sdk'`` if it is found, otherwise ``'damlc'``) or a
        string that identifies a backend.
    :param damlc:
        ``None`` to use the default DAML compiler (``'sdk'`` if it found) or a string that
        identifies a DAML compiler.
    :param time_model_type:
        The mode in which to run the Sandbox clock. Defaults to static time.
    :param ssl_settings:
        Settings that configure how the Sandbox is to start in HTTPS mode. If not supplied, the
        Sandbox starts up in HTTP.
    :param extra_args:
        Extra arguments to pass to the Sandbox.
    :param damlc_extra_args:
        Extra arguments to pass to the compiler (only used when compilation is performed as part
        of running the Sandbox).
    :return:
        A ``SandboxRunner`` that can be used as a context object to end the process.
    """
    # provide default values for backend and port if they were not provided
    if daml_path is None:
        raise ValueError('daml_path is required')

    if port is None:
        from ..util.io import find_free_port
        port = find_free_port()

    full_extra_args = [] if not extra_args else list(extra_args)
    if time_model_type == StaticTimeModel:
        pass
    elif time_model_type == RealTimeModel:
        full_extra_args.append('-w')
    if ssl_settings:
        if ssl_settings.cert_file:
            full_extra_args.extend(('--crt', ssl_settings.cert_file))
        if ssl_settings.cert_key_file:
            full_extra_args.extend(('--pem', ssl_settings.cert_key_file))
        if ssl_settings.ca_file:
            full_extra_args.extend(('--cacrt', ssl_settings.ca_file))

    if isinstance(daml_path, str):
        daml_path = [daml_path]
    elif isinstance(daml_path, Path):
        daml_path = [str(daml_path)]

    options = SandboxOptions(files=daml_path, port=port, extra_args=full_extra_args)
    proc_opts = _sandbox(options, backend, damlc_component=damlc, damlc_extra_args=damlc_extra_args)
    pw = ProcessWatcher(proc_opts)
    pw.extra_data = proc_opts.extra_data
    pw.url = f'http://localhost:{port}'
    return pw


@dataclass(frozen=True)
class _SandboxIntermediateOptions:
    args: 'Tuple[str]'
    context: 'Optional[ContextManager]'
    files: 'Collection[str]'


def _sandbox(options: SandboxOptions,
             component: 'Optional[str]' = None,
             damlc_component: 'Optional[str]' = None,
             damlc_extra_args: 'Sequence[str]' = None) \
        -> 'ProcessContext':
    name, path = sdk_component_path(component or 'sandbox')
    if name == 'damlc':
        # older versions of the DAML compiler supported running DAML natively, but this is no
        # longer supported
        raise ValueError('The damlc-based sandbox is no longer supported.')
    elif name == 'sdk':
        # older versions of dazl could use 'da run sandbox' directly, but the DA Assistant will
        # soon be deprecated and equivalent functionality will not be replicated
        raise ValueError('SDK-based running of the sandbox is no longer supported.')
    elif name != 'sandbox':
        # the sandbox is really the only supported backend at this point
        raise ValueError(f'Unknown component type: {component}')

    LOG.debug('Starting sandbox %s...', component)

    # start the JVM-based sandbox, possibly compiling the source files if they are not already
    # .dar packages or .dalf archives
    int_opts = _sandbox_options(options, damlc_component, damlc_extra_args)
    sandbox_jar = next(path.glob('sandbox-*.jar'))

    args = ['java', '-jar', sandbox_jar, *int_opts.args]
    return ProcessContext(
        args, secondary_context=int_opts.context, logger=logging.getLogger('sandbox'),
        watch_port=options.port, extra_data={'files': int_opts.files})


def _sandbox_options(options: 'SandboxOptions',
                     damlc_component: 'Optional[str]',
                     damlc_extra_args: 'Sequence[str]') \
        -> '_SandboxIntermediateOptions':
    from ..util.dar import TemporaryDar

    files = []
    context = ExitStack()
    for file in options.files:
        ext = Path(file).suffix.lower()
        if ext == '.daml':
            # the Java Sandbox needs .daml files to be converted to a package first
            temp_dar = TemporaryDar(
                file, damlc_component=damlc_component, damlc_extra_args=damlc_extra_args)
            files.extend(context.enter_context(temp_dar))
        elif ext == '.dalf':
            files.append(file)
        elif ext == '.dar':
            files.append(file)
        else:
            raise ValueError(f'unknown file type: {ext}')

    return _SandboxIntermediateOptions(
        args=tuple(str(s) for s in [*options.extra_args, '--port', options.port, *files]),
        context=context,
        files=files)


class SandboxError(DazlError):
    """
    Error raised when the Sandbox aborts abnormally.
    """
    def __init__(self, exit_code: int):
        self.exit_code = exit_code
