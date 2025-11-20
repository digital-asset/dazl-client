# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import NamedTuple, Optional

__all__ = ["SdkVersion"]


class SdkVersion(NamedTuple):
    """Helper for parsing SDK version strings."""

    major: int
    minor: int
    patch: int

    @classmethod
    def parse(cls, s: Optional[str]) -> Optional["SdkVersion"]:
        """
        Parse version string like '2.10.1' or 'v3.4.0'.

        Args:
            s: Version string to parse (can be None)

        Returns:
            Parsed SdkVersion or None if invalid/None
        """
        if s is None:
            return None
        s = s.strip()
        if s.startswith("v"):
            s = s[1:]
        if "-" in s:
            s = s[: s.index("-")]
        try:
            parts = s.split(".")
            nums = [int(p) for p in parts]
            while len(nums) < 3:
                nums.append(0)
            return cls(nums[0], nums[1], nums[2])
        except (ValueError, IndexError):
            return None

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
