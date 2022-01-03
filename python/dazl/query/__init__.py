# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Mapping as MappingABC
from typing import Any, Callable, Collection, Dict, Mapping, Optional, Union

from ..damlast.daml_lf_1 import TypeConName
from ..damlast.lookup import parse_type_con_name
from ..prim import ContractData

__all__ = ["ContractMatch", "is_match", "Query", "Queries", "parse_query", "Filter", "EMPTY"]

ContractMatch = Union[None, Callable[[ContractData], bool], ContractData]

TemplateName = Union[str, "TypeConName"]
Query = Union[None, ContractData, Callable[[ContractData], bool]]
Queries = Union[None, TemplateName, Collection[TemplateName], Mapping[TemplateName, Query]]


class Filter:
    server_side: Optional[ContractData]
    client_side: Optional[Callable[[ContractData], bool]]

    def __init__(
        self,
        *,
        server_side: Optional[ContractData] = None,
        client_side: Optional[Callable[[ContractData], bool]] = None
    ):
        self.server_side = server_side
        self.client_side = client_side

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Filter):
            return False

        return self.server_side == other.server_side and self.client_side == other.client_side


EMPTY = Filter()


def parse_query(*q: Queries, server_side_filters: bool) -> "Optional[Mapping[TypeConName, Filter]]":
    """
    Take a :class:`Queries` object and convert it to a mapping of template names to :class:`Filter`.

    :param q:
        Either:
        * omitted (this means a match on all templates)
        * a single TemplateName (str or TypeConName)
        * a collection of TemplateNames
        * a mapping of TemplateNames to:
            * query objects as defined in https://docs.daml.com/json-api/search-query-language.html
            * functions that perform client-side filtering of contract data
    :param server_side_filters:
        ``True`` to possibly create :class:`Filter` objects with a ``Filter.server_side`` property
        defined (as defined in https://docs.daml.com/json-api/search-query-language.html); ``False``
        to implement all filters as client-side filters.
    :return:
        ``None`` if _all_ templates are to be matched; otherwise a mapping of :class:`TypeConName`
        to :class:`Filter` objects.
    """
    tq = None  # type: Optional[Dict[TypeConName, Filter]]
    for query in q:
        if query is not None and query != "*" and query != "*:*":
            if tq is None:
                tq = {}

            tn = {}  # type: Dict[TypeConName, Filter]
            if isinstance(query, str):
                tn = {parse_type_con_name(query): EMPTY}
            elif isinstance(query, TypeConName):
                tn = {query: EMPTY}
            elif isinstance(query, MappingABC):
                for key, value in query.items():
                    if isinstance(key, str):
                        key = parse_type_con_name(key)
                    tn[key] = _parse_query_filter(value, server_side_filters=server_side_filters)
            else:
                for key in query:
                    if isinstance(key, str):
                        key = parse_type_con_name(key)
                    tn[key] = EMPTY

            tq.update(tn)

    return tq


def _parse_query_filter(__tq: Query, *, server_side_filters: bool) -> Filter:
    if not __tq:
        return EMPTY
    if callable(__tq):
        return Filter(client_side=__tq)
    if server_side_filters:
        return Filter(server_side=__tq)
    else:
        return Filter(client_side=lambda cdata: is_match(__tq, cdata))


def is_match(predicate: ContractMatch, cdata: ContractData) -> bool:
    """
    Determine whether a contract matches a predicate expression.
    """
    if predicate is None:
        return True

    if callable(predicate):
        return predicate(cdata)

    for key, predicate_value in predicate.items():
        cdata_value = cdata.get(key)
        if cdata_value is None:
            # None only matches with None
            if predicate_value is not None:
                return False

        elif callable(predicate_value):
            # support lambdas as predicate values
            if not predicate_value(cdata_value):
                return False

        elif isinstance(predicate_value, dict):
            # deep dictionaries are for variants or records
            return is_match(predicate_value, cdata_value)

        elif predicate_value != cdata_value:
            # exact matches are, of course, supported
            return False

        else:
            # TODO: think of convenient ways to deal with lists
            pass

    return True
