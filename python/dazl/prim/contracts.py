# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Mapping

from ..damlast.daml_lf_1 import TypeConName

__all__ = ["ContractId", "ContractData"]


class ContractId:
    """
    A typed contract ID.

    Instance attributes:

    .. attribute:: ContractId.value

        The raw contract ID value (for example, ``"#4:1"``).

    .. attribute:: ContractId.value_type

        The type of template that is pointed to by this :class:`ContractId`.

    """

    __slots__ = "value", "value_type"

    def __init__(self, value_type: "TypeConName", value: str):
        if not isinstance(value_type, TypeConName):
            raise ValueError("value_type must be a TypeConName")
        if not isinstance(value, str):
            raise ValueError("value must be a string")

        object.__setattr__(self, "value_type", value_type)
        object.__setattr__(self, "value", value)

    def __str__(self):
        """
        Return the contract ID without a type adornment.
        """
        return self.value

    def __repr__(self):
        """
        Return a more detailed view of the ContractId.
        """
        return f"ContractId({self.value_type}, {self.value!r})"

    def __eq__(self, other):
        """
        Returns whether this contract is the same as the other one. Template
        type is NOT considered in equality.
        """
        return isinstance(other, ContractId) and self.value == other.value

    def __format__(self, format_spec):
        """
        Format the ContractId according to the spec.
        """
        return ("{:" + format_spec + "s}").format(self.value)

    def __hash__(self):
        """
        Returns a hash of the ContractId (based on the value of ContractId).
        """
        return hash(self.value)

    def __setattr__(self, key, value):
        """
        Overridden to make ContractId instances read-only.
        """
        raise AttributeError("ContractId instances are read-only")


ContractData = Mapping[str, Any]
