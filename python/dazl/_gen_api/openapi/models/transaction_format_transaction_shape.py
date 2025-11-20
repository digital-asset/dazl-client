from __future__ import annotations

from enum import Enum


class TransactionFormatTransactionShape(str, Enum):
    TRANSACTION_SHAPE_ACS_DELTA = "TRANSACTION_SHAPE_ACS_DELTA"
    TRANSACTION_SHAPE_LEDGER_EFFECTS = "TRANSACTION_SHAPE_LEDGER_EFFECTS"
    TRANSACTION_SHAPE_UNSPECIFIED = "TRANSACTION_SHAPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
