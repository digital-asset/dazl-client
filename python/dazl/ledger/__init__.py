# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.ledger` — gRPC Ledger API / HTTP JSON API client
===========================================================

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
| :class:`CreateAndExerciseCommand` | create a contract and immediately exercise a choice in a     |
|                                   | single transaction                                           |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseCommand`          | exercises a choice on a contract identified by its contract  |
|                                   | ID                                                           |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseByKeyCommand`     | exercises a choice on a contract identified by its contract  |
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

Command types
-------------

.. autoclass:: Command

.. autoclass:: CreateCommand
   :members:

.. autoclass:: CreateAndExerciseCommand
   :members:

.. autoclass:: ExerciseCommand
   :members:

.. autoclass:: ExerciseByKeyCommand
   :members:

Event types
-----------

.. autoclass:: CreateEvent
   :members:

.. autoclass:: ArchiveEvent
   :members:

Other read-side types
---------------------

.. autoclass:: Boundary
   :members:

.. autoclass:: ExerciseResponse
   :members:

Other
-----

.. autoclass:: PartyInfo
    :members:

"""

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
