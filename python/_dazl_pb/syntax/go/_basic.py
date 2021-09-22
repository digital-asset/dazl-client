# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


def public_name(__name: str) -> str:
    """
    Return a string that can be used to refer to the object in a "public" context
    (struct name, function name, public struct field name, etc.).

    >>> public_name('PackageRef')
    'PackageRef'
    >>> public_name('package_ref')
    'PackageRef'
    >>> public_name('Type.Con')
    'Type_Con'
    """
    return "".join(
        ((word[0].upper() + word[1:]) if word else "") for word in __name.split("_")
    ).replace(".", "_")


def private_name(__name: str) -> str:
    """
    Return a string that can be used to refer to the object in a "public" context
    (struct name, function name, public struct field name, etc.).
    """
    pub_name = public_name(__name)
    priv_name = pub_name[0].lower() + pub_name[1:]

    # special-case some private name fields to avoid clashes with Go keywords
    if priv_name == "package":
        return "pkg"
    elif priv_name == "type":
        return "typ"
    elif priv_name == "func":
        return "fn"
    elif priv_name == "range":
        return "rng"
    elif priv_name in ("var", "struct", "nil", "case", "default"):
        return priv_name + "_"

    return priv_name
