# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
:mod:`dazl.ledger` — gRPC Ledger API / HTTP JSON API client
===========================================================
.. autofunction:: connect

This module contains the types needed to submit commands to and read events from a
Daml `gRPC Ledger API <https://docs.daml.com/app-dev/ledger-api.html>`_ or
`HTTP JSON API <https://docs.daml.com/json-api/index.html>`_.

Example:

+-----------------------------------+--------------------------------------------------------------+
| Commands                                                                                         |
+-----------------------------------+--------------------------------------------------------------+
| :class:`Command`                  | abstract base class of all commands                          |
+-----------------------------------+--------------------------------------------------------------+
| :class:`CreateCommand`            | create a contract                                            |
+-----------------------------------+--------------------------------------------------------------+
| :class:`CreateAndExerciseCommand` | create a contract and immediately exercise a choice on the   |
|                                   | newly created contract in a single transaction               |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseCommand`          | exercise a choice on a contract identified by its contract   |
|                                   | ID                                                           |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseByKeyCommand`     | exercise a choice on a contract identified by its contract   |
|                                   | key                                                          |
+-----------------------------------+--------------------------------------------------------------+
| Events and Responses                                                                             |
+-----------------------------------+--------------------------------------------------------------+
| :class:`CreateEvent`              | event raised when a contract is created, either as part of   |
|                                   | the active contract set or on the transaction stream         |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ArchiveEvent`             | event raised when a contract is archived on the transaction  |
|                                   | stream                                                       |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseResponse`         | the response from an exercise, including the choice's return |
|                                   | value (if any)                                               |
+-----------------------------------+--------------------------------------------------------------+
| :class:`Boundary`                 | indicates a point where an event stream can be subsequently  |
|                                   | resumed                                                      |
+-----------------------------------+--------------------------------------------------------------+
| Other                                                                                            |
+-----------------------------------+--------------------------------------------------------------+
| :class:`PartyInfo`                | metadata about a party                                       |
+-----------------------------------+--------------------------------------------------------------+

Write-side types
----------------

Daml ledger state can be updated by submitting commands to the ledger. You should prefer using
:meth:`Connection.create`, :meth:`Connection.create_and_exercise`, :meth:`Connection.exercise`, and
:meth:`Connection.exercise_by_key` over constructing instances of these commands, as those methods
can give you more information about what happened.

.. autoclass:: Command

.. autoclass:: CreateCommand
   :members:

.. autoclass:: CreateAndExerciseCommand
   :members:

.. autoclass:: ExerciseCommand
   :members:

.. autoclass:: ExerciseByKeyCommand
   :members:

Read-side types
---------------

An ``Event`` in a transaction is either a :class:`CreateEvent` or an `ArchiveEvent``.

You can resume a stream of events from a previous point by using ``stream.items()`` and looking for
``Boundary`` objects.

More detailed information about exercises, including the return value and events that occurred as
a result of an exercise, is available from ``ExerciseResponse`` objects as returned from
:meth:`Connection.create_and_exercise`, :meth:`Connection.exercise`, and
:meth:`Connection.exercise_by_key`.

.. autoclass:: CreateEvent
   :members:

.. autoclass:: ArchiveEvent
   :members:

.. autoclass:: Boundary
   :members:

.. autoclass:: ExerciseResponse
   :members:

Other
-----

.. autoclass:: PartyInfo
    :members:

"""
from logging import Logger
from os import PathLike
from typing import Collection, Optional, Union

from ..prim import Party, TimeDeltaLike
from .api_types import (
    ArchiveEvent,
    Boundary,
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    PartyInfo,
)

__all__ = [
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "PartyInfo",
]
