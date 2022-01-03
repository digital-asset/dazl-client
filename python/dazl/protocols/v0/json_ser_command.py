# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Methods for serializing domain objects and other things into basic primitive
types over the wire on the REST interface using JSON.
"""

from datetime import datetime
from typing import TYPE_CHECKING, Any
import warnings

from ...damlast.daml_lf_1 import TypeConName
from ...model.writing import AbstractSerializer
from ...prim import ContractId, JSONEncoder
from ...values.json import JsonEncoder

if TYPE_CHECKING:
    from ...model.writing import CommandPayload

__all__ = ["LedgerJSONEncoder", "to_api_datetime", "JsonSerializer"]


class LedgerJSONEncoder(JSONEncoder):
    """
    Convert some known Ledger API primitive types into their appropriate JSON
    representations.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            "dazl.protocols.v0.json_ser_command.LedgerJSONEncoder is deprecated; "
            "use dazl.prim.JSONEncoder instead.",
            DeprecationWarning,
            stacklevel=2,
        )


def to_api_datetime(obj):
    """
    Converts the object to an ISO8601 datetime string.

    :param obj:
        A datetime. If the datetime is "naive" (no timezone information), it is
        assumed to refer to UTC. If the datetime has timezone information, the
        datetime will be converted to UTC before serializing.
    :return: An ISO8601 string that represents the time in UTC.
    """
    from ...prim import datetime_to_str

    warnings.warn(
        "dazl.protocols.v0.json_ser_command.to_api_datetime is deprecated; "
        "use dazl.prim.datetime_to_str instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return datetime_to_str(obj) if isinstance(obj, datetime) else obj


class JsonSerializer(AbstractSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            "dazl.protocols.v0.json_ser_command.JsonSerializer is deprecated; "
            "there is no replacement.",
            DeprecationWarning,
            stacklevel=2,
        )

    mapper = JsonEncoder()

    def serialize_command_request(self, command_payload: "CommandPayload") -> dict:
        commands = [self.serialize_command(command) for command in command_payload.commands]
        return dict(
            businessIntent=command_payload.command_id,
            commands=commands,
            application=command_payload.application_id,
        )

    def serialize_create_command(self, template_name: "TypeConName", template_args: "Any") -> "Any":
        # the package_id in ModuleRef is a convenient place to
        # stash legacy template IDs in the REST endpoint
        return {"create": {"template": str(template_name), "arguments": template_args}}

    def serialize_exercise_command(
        self, contract_id: ContractId, choice_name: str, choice_args: "Any"
    ) -> "Any":
        return {
            "exercise": {
                "contract": contract_id.value,
                "choice": choice_name,
                "arguments": choice_args,
            }
        }
