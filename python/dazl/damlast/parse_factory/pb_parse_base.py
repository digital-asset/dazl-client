# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence

from .. import daml_lf_1 as lf

__all__ = ["ProtobufParserBase"]


class ProtobufParserBase(ABC):
    """
    Abstract base class for all DAML-LF protobuf parsers.

    Defines the interface that version-specific parsers must implement.
    Each parser converts version-specific protobuf messages to the common AST (daml_lf_1).
    """

    def __init__(self, current_package: lf.PackageRef) -> None:
        self.current_package = current_package
        self.current_module: Optional[lf.ModuleRef] = None
        self.interned_strings: list[str] = []
        self.interned_dotted_names: list[Sequence[str]] = []
        self.interned_types: list[lf.Type] = []

    @abstractmethod
    def parse_Package(self, pb: Any) -> lf.Package:
        """Parse a Package protobuf message."""
        ...

    # Helper methods that may be common across versions
    def _resolve_string(self, direct: str, interned: int) -> str:
        """Resolve a string that may be direct or interned."""
        if direct:
            return direct
        return self.interned_strings[interned]

    def _resolve_string_seq(self, direct: Sequence[str], interned: Optional[int]) -> Sequence[str]:
        """Resolve a sequence of strings that may be direct or interned."""
        if direct:
            return tuple(direct)
        if interned is not None:
            return self.interned_dotted_names[interned]
        return ()

    def _resolve_dotted_name(self, direct: Any, interned: int) -> lf.DottedName:
        """Resolve a DottedName that may be direct or interned."""
        if direct and hasattr(direct, "segments"):
            return lf.DottedName(segments=direct.segments)
        return lf.DottedName(segments=self.interned_dotted_names[interned])
