# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import AbstractSet, Any, Collection, Protocol, Union, runtime_checkable

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

__all__ = ["PackageProvider", "SymbolLookup", "TemplateOrInterface"]


TemplateOrInterface = Union[DefTemplate, DefInterface]


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

    def data_type_name(self, ref: Any) -> TypeConName:
        """
        Return the :class:`TypeConName` that refers to a :class:`DefDataType` that is known to
        exist in this lookup.

        If this method succeeds, :meth:`data_type` with the returned :class:`TypeConName` as an
        argument should also always succeed.
        """
        raise NotImplementedError("SymbolLookup.data_type_name must be implemented")

    def data_type(self, ref: Any) -> DefDataType:
        """
        Return the :class:`DefDataType` for the specified name.
        """
        raise NotImplementedError("SymbolLookup.data_type must be implemented")

    def value(self, ref: Any) -> DefValue:
        """
        Return the :class:`DefValue` for the specified name.
        """
        raise NotImplementedError("SymbolLookup.value must be implemented")

    def template_names(self, ref: Any) -> Collection[TypeConName]:
        """
        Return all template names that are currently known that are a match for the query. Either
        :class:`PackageRef` or the template name can be `*`.

        Unlike the other methods of this class, this function should return an empty list in the
        case of a match failure; :class:`PackageNotFoundError` or :class:`NameNotFoundError` are
        never thrown.
        """
        raise NotImplementedError("SymbolLookup.template_names must be implemented")

    def template_name(self, ref: Any) -> TypeConName:
        """
        Return the :class:`TypeConName` that refers to a :class:`DefTemplate` that is known to
        exist in this lookup.

        If this method succeeds, :meth:`template` with the returned :class:`TypeConName` as an
        argument should also always succeed.
        """
        raise NotImplementedError("SymbolLookup.template_name must be implemented")

    def template(self, ref: Any) -> DefTemplate:
        """
        Return the :class:`DefTemplate` for the specified name.
        """
        raise NotImplementedError("SymbolLookup.template must be implemented")

    def interface_names(self, ref: Any) -> Collection[TypeConName]:
        """
        Return all template names that are currently known that are a match for the query.
        The :class:`PackageRef` can be `*`.

        Unlike the other methods of this class, this function should return an empty list in the
        case of a match failure; :class:`PackageNotFoundError` or :class:`NameNotFoundError` are
        never thrown.
        """
        raise NotImplementedError("SymbolLookup.interface_names must be implemented")

    def interface_name(self, ref: Any) -> TypeConName:
        """
        Return the :class:`TypeConName` that refers to a :class:`DefInterface` that is known to
        exist in this lookup.

        If this method succeeds, :meth:`interface` with the returned :class:`TypeConName` as an
        argument should also always succeed.
        """
        raise NotImplementedError("SymbolLookup.interface_name must be implemented")

    def interface(self, ref: Any) -> DefInterface:
        """
        Return the :class:`DefInterface` for the specified name.
        """
        raise NotImplementedError("SymbolLookup.interface must be implemented")

    def template_or_interface_names(self, ref: Any) -> Collection[TypeConName]:
        """
        Return all template or interface names that are currently known that are
        a match for the query. Either :class:`PackageRef` or the template name
        can be `*`. When using `*`, only templates are searched.

        Unlike the other methods of this class, this function should return an
        empty list in the case of a match failure; :class:`PackageNotFoundError`
        or :class:`NameNotFoundError` are never thrown.
        """
        raise NotImplementedError("SymbolLookup.template_or_interface_names must be implemented")

    def template_or_interface_name(self, ref: Any) -> TypeConName:
        """
        Return the :class:`TypeConName` that refers to a :class:`DefTemplate` or
        :class:`DefInterface` that is known to exist in this lookup.

        If this method succeeds, :meth:`template_or_interface` with the returned
        :class:`TypeConName` as an argument should also always succeed.
        """
        raise NotImplementedError("SymbolLookup.interface_name must be implemented")

    def template_or_interface(self, ref: Any) -> TemplateOrInterface:
        """
        Return the :class:`DefTemplate` or :class:`DefInterface` for the specified name.
        """
        raise NotImplementedError("SymbolLookup.template must be implemented")
