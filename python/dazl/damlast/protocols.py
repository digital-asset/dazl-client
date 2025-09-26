# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, AbstractSet, Any, Collection, Protocol, runtime_checkable
import warnings

from .daml_lf_1 import (
    Archive,
    DefDataType,
    DefInterface,
    DefTemplate,
    DefValue,
    Package,
    PackageRef,
    TypeConName,
)

if sys.version_info >= (3, 11):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from .lookup import LookupResult

__all__ = ["PackageProvider", "SymbolLookup", "TemplateOrInterface"]


TemplateOrInterface = DefTemplate | DefInterface


@runtime_checkable
class PackageProvider(Protocol):
    """
    Structural interface for a class that can synchronously provide package data.

    If a requested package could not be found, :class:`PackageNotFoundError` should be raised; the
    functions of this protocol should never return ``None``.
    """

    def package(self, ref: PackageRef) -> Package:
        """
        Return the :class:`Package` for the specified :class:`PackageRef`.

        :param ref:
            The package ID to look up.
        :return:
            The Package corresponding to this package ID.
        :raises PackageNotFoundError:
            if the package could not be found
        """
        raise NotImplementedError("PackageProvider.package must be implemented")

    def package_ids(self) -> AbstractSet[PackageRef]:
        """
        Return all package IDs that are known to this :class:`PackageProvider`.

        Implementations are allowed to return larger sets of packages over time, but should
        generally never omit a package ID that was previously returned.

        :return:
            A set of package IDs.
        """
        raise NotImplementedError("PackageProvider.package_ids must be implemented")


@runtime_checkable
class SymbolLookup(Protocol):
    """
    Structural interface for a class that can synchronously provide type/value information.

    If a requested _package_ could not be found, :class:`PackageNotFoundError` is raised.
    If a requested package is known to this :class:`SymbolLookup` but the name is unknown, then
    :class:`NameNotFoundError` is raised. Callers can use this to disambiguate between errors that
    are retryable (missing packages can be fetched) and non-retryable (names within a known package,
    if they do not currently exist, will NEVER exist).
    """

    def archives(self) -> Collection[Archive]:
        """
        Return the archives that are known to this lookup.
        """
        raise NotImplementedError("SymbolLookup.archives must be implemented")

    def package_ids(self) -> AbstractSet[PackageRef]:
        """
        Return the package IDs that are known to this lookup.
        """
        raise NotImplementedError("SymbolLookup.package_ids must be implemented")

    def search(self, ref: str | TypeConName, /, *, throw_if_missing: bool = True) -> LookupResult:
        """
        Search for matching templates or interfaces. Throws
        :class:`PackageNotFoundError` or :class:`NameNotFoundError` if nothing
        has been found.

        :param ref:
            The string or :class:`TypeConName` to search for.
        :param throw_if_missing:
            Throw a :class:`NameNotFoundError` if no objects are returned; otherwise,
            return an empty object. The default behavior is to throw.
        :return:
            A :class:`LookupResult` that contains the results of the search. It
            will always contain at least one match.
        """
        raise NotImplementedError("SymbolLookup.search must be implemented")
