# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module is considered an implementation detail and may change at any time.
Use at your own risk!
"""

from logging import Logger, getLogger
import os
from typing import (
    Any,
    Collection,
    Generic,
    List,
    Mapping,
    Optional,
    Sequence,
    TypeVar,
    Union,
)

from ...prim import Party, to_bool
from .exc import ConfigError

T = TypeVar("T", covariant=True)
Parties = Union[None, Party, Collection[Party]]


class Validator:
    """
    Validate that only one configuration option out of a group is provided.
    """

    def __init__(self, logger: Optional[Logger]):
        self.logger = logger if logger is not None else getLogger("dazl.conn")
        self.cases = []  # type: List[Case]

    def new_case(self, name: str) -> "Case":
        case = Case(name)
        self.cases.append(case)
        return case

    def validate(self) -> Optional[str]:
        """
        Validate that configured values satisfy only zero or one cases.
        """
        if not self.cases:
            raise ValueError("Validator created without cases")

        # if any _actual_ values were supplied for any of our cases, then use those
        matching_cases = [case for case in self.cases if case.has_values()]
        if len(matching_cases) > 1:
            # multiple conflicting options provided
            self.logger.error("Found conflicting configuration:")
            for case in self.cases:
                values = case.values()
                if values:
                    self.logger.error("  %s:", case.name)
                    for k, v in values.items():
                        self.logger.error("    %s=%s", k, v)
            self.logger.error("Specify ONLY")
            raise ConfigError("")

        if len(matching_cases) == 1:
            return matching_cases[0].name

        # no options were specified across the board; try again using values from the
        # environment
        for case in self.cases:
            case.read_environment()

        matching_cases = [case for case in self.cases if case.has_values()]
        if len(matching_cases) > 1:
            # we are going to fail because multiple conflicting environment variables have
            # been specified; log something nice first before failing
            self.logger.error("Found conflicting environment variables:")
            for case in self.cases:
                env_vars = case.environment()
                if env_vars:
                    self.logger.error("  %s:", case.name)
                    for k, v in env_vars.items():
                        self.logger.error("    %s=%s", k, v)
            self.logger.error(
                "Define environment variables from only one of these groups, "
                "or pass explicit config instead!"
            )
            raise ConfigError("")

        if len(matching_cases) == 1:
            return matching_cases[0].name

        # no values passed in, no values provided from the environment
        return None


class Case:
    """
    A configuration "possibility".

    Within a given set of config groups, only one :class:`Case` is allowed to be provided at a time.
    If _no_ values are directly provided, environment variables may be consulted.
    """

    def __init__(self, name):
        self.name = name
        self.fields = []  # type: List[Value[Any]]

    def __enter__(self) -> "Case":
        """
        Allow :class:`Case` to be used with the ``with`` keyword. Syntactically it makes "cases"
        stand out a little better, even though we don't really use the context manager for anything.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closing method for the context manager.
        """

    def boolean(self, field: str, value: Optional[bool], *env_vars: str) -> "Value[bool]":
        v = BooleanValue(field, value, env_vars)
        self.fields.append(v)
        return v

    def int(self, field: str, value: Optional[int], *env_vars: str) -> "Value[int]":
        v = IntValue(field, value, env_vars)
        self.fields.append(v)
        return v

    def string(self, field: str, value: Optional[str], *env_vars: str) -> "Value[str]":
        v = StrValue(field, value, env_vars)
        self.fields.append(v)
        return v

    def parties(self, field: str, value: Parties, *env_vars: str) -> "Value[Collection[Party]]":
        """
        Add a "parties"-valued field to this case.
        """
        if value is None:
            party_values = []  # type: Sequence[Party]
        elif isinstance(value, str):
            party_values = [Party(item) for item in value.split(",")] if value else []
        else:
            party_values = list(value)

        v = PartiesValue(field, party_values, env_vars)
        self.fields.append(v)
        return v

    def values(self) -> Mapping[str, Any]:
        return {field.name: field.value for field in self.fields}

    def has_values(self) -> bool:
        """
        Determine if any fields have supplied values for this case.
        """
        return any(field.has_value() for field in self.fields)

    def environment(self):
        env_vars = {}

        for field in self.fields:
            for key in field.env_vars:
                value = os.getenv(key, "")
                if value:
                    env_vars[key] = value
        return env_vars

    def read_environment(self):
        """
        Imperatively read the environment and apply any relevant environment variables to their
        respective fields.
        """
        for field in self.fields:
            for key in field.env_vars:
                value = os.getenv(key, "")
                if value:
                    field.env_setter(value)


class Value(Generic[T]):
    def __init__(self, name: str, value: Optional[T], env_vars: Sequence[str]):
        self.name = name
        self.value = value
        self.env_vars = env_vars

    def env_setter(self, env_value: str) -> None:
        raise NotImplementedError

    def has_value(self) -> bool:
        raise NotImplementedError


class BooleanValue(Value[bool]):
    def env_setter(self, env_value: str) -> None:
        self.value = to_bool(env_value)

    def has_value(self) -> bool:
        return self.value is not None


class IntValue(Value[int]):
    def env_setter(self, env_value: str) -> None:
        self.value = int(env_value)

    def has_value(self) -> bool:
        return self.value is not None


class StrValue(Value[str]):
    def env_setter(self, env_value: str) -> None:
        self.value = env_value

    def has_value(self) -> bool:
        return bool(self.value)


class PartiesValue(Value[Collection[Party]]):
    def env_setter(self, env_value: str) -> None:
        self.value = [Party(party) for party in env_value.split(',') if party]

    def has_value(self) -> bool:
        return bool(self.value)
