# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional, Sequence, Union

from ..config import Config

__all__ = ["Connection"]

from ...prim import JSONEncoder


class Connection:
    def __init__(self, config: "Config"):
        self.config = config

    def open(self):
        self.conn

    def submit(
        self,
        __commands: "Union[Command, Sequence[Command]]",
        *,
        workflow_id: "Optional[str]" = None,
        command_id: "Optional[str]" = None,
    ) -> "None":
        pass

    def create(
        self,
        __template_id: "Union[str, TypeConName]",
        __payload: "ContractData",
        *,
        workflow_id: "Optional[str] = None",
        command_id: "Optional[str] = None",
    ) -> "CreateEvent":
        encoder = JSONEncoder()

        body = encoder.encode({"templateId": str(__template_id), "payload": __payload})
        self.conn.request("POST", f"{self.config.url.url}/v1/create", body)
        r = self.conn.getresponse()
        decode_created_event()
        r.result

    def exercise(self):
        {"templateId", "contractId", "choice", "argument"}
