# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Core types
----------

The :mod:`dazl.model.core` module contains classes used on both the read-side and the write-side of
the Ledger API.

.. autoclass:: ContractId
   :members:
"""
import warnings
from dataclasses import dataclass
from typing import Any, Callable, Collection, Dict, List, NewType, Optional, Tuple, TypeVar, \
    Union, TYPE_CHECKING
from datetime import datetime

from ..util.enum import OrderedEnum

if TYPE_CHECKING:
    from .types import Type

T = TypeVar('T')


class ContractId:
    """
    There are two kinds of contract IDs: those that know the template type of the underlying
    contract instance and those that don't. Contract IDs that arise from event processing are always
    tagged with their type when they are read off the event stream. Contract IDs that are
    parameters to a template are not currently tagged with a template type.

    Instance attributes:

    .. attribute:: ContractId.contract_id

        A ``str`` reference to a contract.

    .. attribute:: ContractId.template_id

        An optional ``str`` template ID.

    Instance members:
    """
    __slots__ = ('contract_id', 'template_id')

    def __init__(self, contract_id: str, template_id: 'Union[None, str, Type]' = None):
        from .types import Type, UnresolvedTypeReference
        if not isinstance(contract_id, str):
            raise ValueError('contract_id must be a string')

        if template_id is None:
            warnings.warn('Untyped ContractId support will be removed with the removal of '
                          'the deprecated REST API.', DeprecationWarning, stacklevel=2)
        else:
            if isinstance(template_id, str):
                template_id = UnresolvedTypeReference(template_id)
            elif not isinstance(template_id, Type):
                raise ValueError(f'template_id must either be unspecified or a template identifier '
                                 f'(got {repr(template_id)})')

        self.contract_id = contract_id
        self.template_id = template_id

    def __str__(self):
        """
        Return the contract ID without a type adornment.
        """
        return self.contract_id

    def __repr__(self):
        if self.template_id is not None:
            return '<ContractId("{}<{}>")>'.format(self.contract_id, self.template_id)
        else:
            return '<ContractId("{}")>'.format(self.contract_id)

    def __eq__(self, other):
        """
        Returns whether this contract is the same as the other one. Template
        type is NOT considered in equality.
        """
        return isinstance(other, ContractId) and self.contract_id == other.contract_id

    def __format__(self, format_spec):
        return ('{:' + format_spec + 's}').format(self.contract_id)

    def __hash__(self):
        """
        Returns a hash of the ContractId (based on the value of ContractId).
        """
        return hash(self.contract_id)

    def exercise(self, choice_name, arguments=None):
        """
        Create an :class:`ExerciseCommand` that represents the result of exercising a choice on this
        contract with the specified choice.

        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            (optional) A ``dict`` of named values to send as parameters to the choice exercise.
        """
        from .writing import ExerciseCommand
        return ExerciseCommand(self, choice_name, arguments=arguments)

    def replace(self, contract_id=None, template_id=None):
        """
        Return a new :class:`ContractId` instance replacing specified fields with values.
        """
        return ContractId(
            contract_id if contract_id is not None else self.contract_id,
            template_id if template_id is not None else self.template_id)

    def for_json(self):
        """
        Return the JSON representation of this contract. This is currently just the contract ID
        string itself.
        """
        return self.contract_id


ContractData = Dict[str, Any]
ContractMatch = Union[None, Callable[[ContractData], bool], ContractData]
ContractsState = Dict[ContractId, ContractData]
ContractsHistoricalState = Dict[ContractId, Tuple[ContractData, bool]]
Party = NewType('Party', str)


class ContractContextualDataCollection(tuple):

    def __getitem__(self, index: Union[int, str, ContractId]):
        if index is None:
            raise ValueError('the index cannot be None')
        elif isinstance(index, int):
            return tuple.__getitem__(self, index)
        elif isinstance(index, str):
            for cxd in self:
                if cxd.cid.contract_id == index:
                    return cxd
            raise KeyError(index)
        elif isinstance(index, ContractId):
            for cxd in self:
                if cxd.cid == index:
                    return cxd
            raise KeyError(index)
        else:
            raise TypeError("cannot index into a ContractContextualDataCollection with {index!r}")


@dataclass(frozen=True)
class ContractContextualData:
    cid: ContractId
    cdata: 'Optional[ContractData]'
    effective_at: datetime
    archived_at: 'Optional[datetime]'
    active: bool


@dataclass(frozen=True)
class SourceLocation:
    file_name: str
    start_line: int
    end_line: int


class RunLevel(OrderedEnum):
    RUN_FOREVER = 0
    RUN_UNTIL_IDLE = 1
    TERMINATE_GRACEFULLY = 2
    TERMINATE_IMMEDIATELY = 3
    STOPPED = 4


class DazlError(Exception):
    """
    Superclass of errors raised by dazl.
    """


class DazlWarning(Warning):
    """
    Superclass of warnings raised by dazl.
    """


class DazlPartyMissingError(DazlError):
    """
    Error raised when a party or some information about a party is requested, and that party is not
    found.
    """
    def __init__(self, party: Party):
        super().__init__(f'party {party!r} does not have a defined client')
        self.party = party


class DazlImportError(ImportError, DazlError):
    """
    Import error raised when an optional dependency could not be found.
    """
    def __init__(self, missing_module, message):
        super().__init__(message)
        self.missing_module = missing_module


class UserTerminateRequest(DazlError):
    """
    Raised when the user has initiated a request to terminate the application.
    """


class ConnectionTimeoutError(DazlError):
    """
    Raised when a connection failed to be established before the connection timeout elapsed.
    """


class CommandTimeoutError(DazlError):
    """
    Raised when a corresponding event for a command was not seen in the appropriate time window.
    """


class ConfigurationError(DazlError):
    """
    Raised when a configuration error prevents a client from being started.

    .. attribute:: ConfigurationError.reasons

        A collection of reasons for a failure.
    """
    def __init__(self, reasons: 'Union[str, Collection[str]]'):
        if reasons is None:
            self.reasons = []  # type: List[str]
        elif isinstance(reasons, str):
            self.reasons = [reasons]
        else:
            self.reasons = reasons  # type: List[str]


class ConnectionClosedError(DazlError):
    """
    Raised when trying to do something that requires a connection after connection pools have been
    closed.
    """


class UnknownTemplateWarning(DazlWarning):
    """
    Raised when trying to do something with a template name that is unknown.
    """


class ProcessDiedException(DazlError):
    pass
