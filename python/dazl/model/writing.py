# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module has been relocated to ``dazl.client.commands``, though if possible you should move to
the command types defined in ``dazl.ledger`` instead.
"""
import warnings

from ..client.commands import (
    CommandBuilder,
    CommandDefaults,
    CommandPayload,
    CommandsOrCommandSequence,
    CreateAndExerciseCommand,
    CreateCommand,
    EventHandlerResponse,
    ExerciseByKeyCommand,
    ExerciseCommand,
    create,
    create_and_exercise,
    exercise,
    exercise_by_key,
    flatten_command_sequence,
)
from ..ledger import Command
from ..protocols.serializers import AbstractSerializer, Serializer

warnings.warn(
    "dazl.model.writing is deprecated; please use the types of dazl.ledger.api_types instead.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "AbstractSerializer",
    "Command",
    "CommandBuilder",
    "CommandDefaults",
    "CommandPayload",
    "CommandsOrCommandSequence",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "EventHandlerResponse",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "Serializer",
    "create",
    "create_and_exercise",
    "exercise",
    "exercise_by_key",
    "flatten_command_sequence",
]
