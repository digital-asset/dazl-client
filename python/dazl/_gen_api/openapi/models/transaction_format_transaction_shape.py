# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from enum import Enum


class TransactionFormatTransactionShape(str, Enum):
    TRANSACTION_SHAPE_ACS_DELTA = "TRANSACTION_SHAPE_ACS_DELTA"
    TRANSACTION_SHAPE_LEDGER_EFFECTS = "TRANSACTION_SHAPE_LEDGER_EFFECTS"
    TRANSACTION_SHAPE_UNSPECIFIED = "TRANSACTION_SHAPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
