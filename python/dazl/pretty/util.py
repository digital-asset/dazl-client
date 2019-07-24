# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Sequence


def unmangle_name(s: str) -> str:
    """
    Convert a name with ``$uXXXX`` character runs into their original forms, which may not
    necessarily be safe DAML identifiers.

    :param s: The string to interpret.
    :return: A new string with the appropriate substitutions.
    """
    return s.replace('$u002b', '+').replace('$u005b', '[').replace('$u005d', ']'). \
        replace('$u003c', '<').replace('$u003e', '>').replace('$u003a', ':'). \
        replace('$u0022', '"').replace('$u0028', '(').replace('$u0029', ')'). \
        replace('$u002f', '/').replace('$u002c', ',').replace('$u003d', '=')


def is_hidden_module_name(name: 'Sequence[str]') -> bool:
    if len(name) == 1 and name[0] in ('GhcPrim', 'Prelude'):
        return True
    if len(name) >= 2:
        if name[0] == 'GHC':
            return True
        elif name[0] == 'DA':
            return True
        elif name[0] == 'Control' and name[1] == 'Exception':
            return True
    return False


def maybe_parentheses(obj, operator: str = ' ') -> str:
    """
    Wrap the string (or object's string representation) in parentheses, but only if required.
    :param obj:
        The object to (potentially) wrap up in parentheses. If it is not a string, it is converted
        to a string first.
    :param operator:
        The operator that needs precedence rules clarified. The default is ``' '`` (a space).
    :return: The (possibly) parenthesized string.
    """
    s = str(obj)
    if operator not in s:
        return s

    # if there are already wrapping punctuation marks, there may not be a need to add additional
    # ones
    open_mark = s[0]
    if open_mark in '([{':
        groupings = [s[0]]
        for c in s[1:-1]:
            if c in '([{':
                groupings.append(c)
            elif c == '}':
                if groupings[-1] == '{':
                    groupings.pop()
                else:
                    groupings.clear()
            elif c == ']':
                if groupings[-1] == '[':
                    groupings.pop()
                else:
                    groupings.clear()
            elif c == ')':
                if groupings[-1] == '(':
                    groupings.pop()
                else:
                    groupings.clear()

            if not groupings:
                # we balanced out all groupings (or just his a syntax error in unmatched groupings);
                # add clarifying parentheses
                return '(' + s + ')'
        if (groupings[0] == '(' and groupings[-1] == ')') or \
           (groupings[0] == '[' and groupings[-1] == ']') or \
           (groupings[0] == '{' and groupings[-1] == '}'):
            return s
    return '(' + s + ')' if operator in s else s


def indent(text: str, spaces: int):
    """
    Prepend every line of the specified text with a set number of spaces. Line endings are
    preserved.
    """
    prefix = ' ' * spaces
    return ''.join(prefix + t for t in text.splitlines(keepends=True))
