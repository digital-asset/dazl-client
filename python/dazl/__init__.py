# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the Python API for interacting with the Ledger API.
"""


import pkg_resources as _pkg_resources
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .util.logging import LoggerWithVerbose


def _initialize_logger() -> 'LoggerWithVerbose':
    import logging
    from .util.logging import _LoggerWithVerbose, log_verbose

    try:
        # noinspection PyPackageRequirements
        import google

        # This method is undocumented, but is required to read large size of model files when using
        # the C++ implementation.
        # noinspection PyPackageRequirements,PyUnresolvedReferences,PyProtectedMember
        from google.protobuf.pyext import _message
        _message.SetAllowOversizeProtos(True)

    except ImportError:
        pass

    original_logger = logging.getLoggerClass()

    class CombinedLogger(original_logger, _LoggerWithVerbose):
        pass

    logging.setLoggerClass(CombinedLogger)
    dazl_logger = logging.getLogger('dazl')
    if not hasattr(dazl_logger, 'verbose'):
        from functools import partial
        dazl_logger.verbose = partial(log_verbose, dazl_logger)
    logging.setLoggerClass(original_logger)
    return dazl_logger


LOG = _initialize_logger()  # type: LoggerWithVerbose


from .damlsdk.sandbox import sandbox  # noqa
from .client import run, simple_client, Network, SimplePartyClient, AIOPartyClient  # noqa
from .model.core import ContractId, DazlError, Party  # noqa
from .model.types import module, TemplateMeta, ChoiceMeta  # noqa
from .model.writing import create, exercise, exercise_by_key, create_and_exercise, \
    Command, CreateCommand, ExerciseCommand, ExerciseByKeyCommand, CreateAndExerciseCommand  # noqa
from .util.logging import setup_default_logger  # noqa
from .util.prim_types import frozendict  # noqa
from .plugins.capture.plugin_capture import write_acs  # noqa


__version__ = _pkg_resources.require('dazl')[0].version
