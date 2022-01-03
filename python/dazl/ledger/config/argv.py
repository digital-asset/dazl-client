# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Support for exposing dazl's configuration parameters through :mod:`argparse`.
"""
import argparse
from argparse import SUPPRESS, Action, ArgumentParser
import os
import sys
from typing import TYPE_CHECKING, Optional, Sequence
import warnings

from .exc import ConfigWarning
from .url import DEFAULT_CONNECT_TIMEOUT, KNOWN_SCHEME_PORTS

if TYPE_CHECKING:
    from argparse import _ArgumentGroup

__all__ = ["configure_parser", "EXAMPLES"]


# Implementation notes:
#
# A common trick employed throughout this file is to add an "argument" to a parser that is not
# directly used. Calling ``add_arguments(...)`` with a "name" of a completely arbitrary string that
# is not practically possible to be called from the command line (for example,
# ``add_arguments("--my-special-flag SOMETHING | -m BLAH")`` is entirely allowed. This also renders
# as-is in the help strings. Additionally, passing nargs=SUPPRESS essentially prevents the flag from
# being used during parsing, but does NOT remove it from help! The opposite (passing help=SUPPRESS)
# can be used to hide the "real" arguments from the help string that would otherwise render in an
# ugly way. This leads to this:
#
#   # argparse does not support different metavars for different arguments, so one arg for the
#   # help string we want, and two more args for the two different cases
#   parser.add_argument("--something STUFF | --something-file TOKEN", nargs=SUPPRESS)
#   parser.add_argument("--something", help=SUPPRESS, ...)
#   parser.add_argument("--something-file", help=SUPPRESS, ...)

# An example string that can be used to help illustrate how to use common flags.
EXAMPLES = """
  # connect to a local sandbox acting as Alice and Bob, with Carol read-only
  # (localhost is the default if no url/host is specified)
  %(prog)s -u Alice,Bob -r Carol

  # connect to myledger.daml.app over SSL/TLS using the access token in "token.txt"
  %(prog)s --url https://myledger.daml.app/ --oauth-token-file token.txt
"""


class WideHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog: str, *args, **kwargs):
        if "max_help_position" not in kwargs:
            kwargs["max_help_position"] = 43
        if "width" not in kwargs:
            col = os.getenv("COLUMNS")
            if col:
                kwargs["width"] = int(col)

        super().__init__(prog, *args, **kwargs)

    # Backport a formatting fix for Python 3.6
    if sys.version_info < (3, 7):

        def _format_args(self, action: Action, default_metavar: str) -> str:
            if action.nargs == SUPPRESS:
                return ""
            else:
                # noinspection PyProtectedMember
                return super()._format_args(action, default_metavar)


def configure_parser(parser: ArgumentParser, add_usage: bool = True) -> None:
    """
    Add dazl configuration options to an existing :class:`ArgumentParser`.

    dazl exposes a variety of configuration options that could be tedious to duplicate in your own
    application. To use this in your own application:

    .. code-block:: python

        parser = argparse.ArgumentParser(description='Something awesome with dazl.')
        configure_parser(parser)
        args = parser.parse_args()

        conn = dazl.connect(**args)

    :param parser:
        The :class:`ArgumentParser` to add options to.
    :param add_usage:
        ``True`` to overwrite the usage string with something more compact; because there are a
        lot of variables, the default usage string doesn't add much
    """
    if add_usage:
        parser.usage = "%(prog)s [OPTIONS]\n\n" + EXAMPLES

    _configure_url_basic_options(parser)
    _configure_access(parser)
    _configure_url_advanced_options(parser)
    _configure_deprecated_options(parser)


def _configure_access(parser: ArgumentParser):
    group_p = parser.add_argument_group("Access configuration (property-based)")

    group_p.add_argument("--act-as/-u PARTY [PARTY ...]", nargs=SUPPRESS, help="act-as parties")
    group_p.add_argument(
        "--act-as",
        "-u",
        "--party",
        "--parties",
        help=SUPPRESS,
        action=AppendPartySetAction,
    )
    group_p.add_argument("--read-as/-r PARTY [PARTY ...]", nargs=SUPPRESS, help="read-as parties")
    group_p.add_argument(
        "--read-as",
        "-r",
        "--party-groups",
        help=SUPPRESS,
        action=AppendPartySetAction,
    )

    group_p.add_argument(
        "--admin",
        action="store_const",
        const=True,
        help="Add admin flag (HTTP JSON API only)",
    )
    group_p.add_argument(
        "--ledger-id",
        "-l",
        help="ledger ID (required on HTTP JSON API)",
    )
    group_p.add_argument(
        "--application-name",
        metavar="NAME",
        help="application name; uniquely identifies this client to the server",
    )

    group_t = parser.add_argument_group("Access configuration (token-based)")
    add_text_or_file_argument(
        group_t,
        "--oauth-token",
        metavar="TOKEN",
        help="OAuth2 bearer token",
    )


def _configure_url_basic_options(parser: ArgumentParser):
    url = parser.add_argument_group("Basic options")
    url.add_argument(
        "--url",
        help="URL of the gRPC Ledger API/HTTP JSON API (cannot be used with --host/--port)",
    )
    # kept around for backwards compatibility
    url.add_argument("--participant-url", dest="url", help=argparse.SUPPRESS)

    host_help = "ledger host (cannot be used with --url; default: localhost)"
    url.add_argument("--host/-H HOST", help=host_help, nargs=SUPPRESS)
    url.add_argument("--host", "-h", help=SUPPRESS)

    # The --port field. Note that -p used to mean parties, but now it means port; this is a little
    # hook to preserve backwards compatibility for one version (as it turns out, the value of the
    # -p flag CAN disambiguate usage so we keep the CLI user-friendly, even it gets a little ugly
    # under the hood for dazl v8
    port_help = "ledger port (cannot be used with --url; default: based on scheme/host)"
    url.add_argument("--port/-p PORT", help=port_help, nargs=SUPPRESS)
    url.add_argument("--port", metavar="PORT", help=SUPPRESS, type=int)
    url.add_argument("-p", action=DashPAction, help=SUPPRESS)

    url.add_argument(
        "--scheme",
        help="scheme/protocol (cannot be used with --url)",
        choices=KNOWN_SCHEME_PORTS,
    )


def _configure_url_advanced_options(parser: ArgumentParser):
    group = parser.add_argument_group("Advanced options")
    LOG_LEVELS = ["verbose", "debug", "info", "warn", "error"]
    group.add_argument(
        "--log-level",
        metavar="LEVEL",
        choices=LOG_LEVELS,
        help=f"logging level (one of {{{','.join(LOG_LEVELS)}}}; default: warn)",
    )
    group.add_argument(
        "--connect-timeout",
        metavar="SECONDS",
        type=float,
        help="number of seconds before giving up on a connection "
        f"(default: {DEFAULT_CONNECT_TIMEOUT.total_seconds()})",
    )

    group.add_argument(
        "--plaintext",
        help="force the connection to use plaintext instead of SSL/TLS",
        dest="scheme",
        action="store_const",
        const="http",
    )

    add_text_or_file_argument(
        group,
        "--cert",
        metavar="CERT",
        help="client certificate (mutual TLS)",
    )
    add_text_or_file_argument(
        group,
        "--cert-key",
        metavar="CERT",
        help="client certificate private key (mutual TLS)",
    )
    add_text_or_file_argument(
        group,
        "--ca",
        metavar="CA",
        help="certificate authority",
    )
    add_bool_argument(
        group,
        "--use-http-proxy",
        hidden_true_flags=["--enable-http-proxy"],
        help="allow/disallow HTTP proxy server usage (default: use, except for localhost)",
    )
    group.add_argument(
        "--package-fetch-poll-interval",
        metavar="SECONDS",
        type=int,
        help="how frequently to fetch ALL packages (default: 0 [don't periodically fetch])",
    )
    # for backwards compatibility; remove in dazl v9
    group.add_argument(
        "--eager-package-fetch",
        action="store_const",
        dest="package_fetch_poll_interval",
        const=1,
        help=SUPPRESS,
    )


def _configure_deprecated_options(parser: ArgumentParser):
    add_no_effect_deprecated_flag(parser, "--idle-timeout")
    add_no_effect_deprecated_flag(parser, "--max-command-batch-timeout")
    add_no_effect_deprecated_flag(parser, "--max-connection-batch-size")
    add_no_effect_deprecated_flag(parser, "--max-connection-count")
    add_no_effect_deprecated_flag(parser, "--max-consequence-depth")
    add_no_effect_deprecated_flag(parser, "--max-event-block-size")
    add_no_effect_deprecated_flag(parser, "--poll-interval")
    add_no_effect_deprecated_flag(parser, "--quiet-count")
    add_no_effect_deprecated_flag(parser, "--use-acs-service", nargs=0)


def add_no_effect_deprecated_flag(parser, *name_or_flags: str, **kwargs):
    """
    Add a flag that can be passed in, but does
    """
    parser.add_argument(
        *name_or_flags,
        action=IgnoreAction,
        warning=f"{'/'.join(name_or_flags)} is no longer used and has no effect; "
        "this flag will be removed in dazl v9",
        help=argparse.SUPPRESS,
        **kwargs,
    )


# noinspection PyShadowingBuiltins
def add_text_or_file_argument(
    parser: "_ArgumentGroup",
    *name_or_flags: str,
    metavar: "Optional[str]" = None,
    metavar_file: str = "FILE",
    help: "Optional[str]" = None,
) -> None:
    """
    Add a (user-facing) argument that can be passed in as a text value on the command-line or as a
    file.

    Note that this actually adds _two_ arguments, one for the base case where a string is passed in
    and another to handle files. This is in line with what :meth:`Config.create` expects.
    """
    if help == SUPPRESS:
        # we may enable this one day, but for now we're the only ones allowed to play weird games
        # with argparse
        raise ValueError("SUPPRESS is not supported here")

    # The first "argument" that we add is actually just for purposes of displaying a nice help
    # string; it is not directly usable
    file_flags = [f"{flag}-file" for flag in name_or_flags if flag.startswith("--")]

    if metavar is None:
        metavar = "STRING"

    parser.add_argument(
        f"{'/'.join(name_or_flags)} {metavar} | {'/'.join(file_flags)} {metavar_file}",
        action=IgnoreAction,
        nargs=SUPPRESS,
        help=help,
    )
    parser.add_argument(*name_or_flags, help=argparse.SUPPRESS)
    parser.add_argument(*file_flags, help=argparse.SUPPRESS)


# noinspection PyShadowingBuiltins
def add_bool_argument(
    parser: "_ArgumentGroup",
    *name_or_flags: str,
    hidden_true_flags: "Optional[Sequence[str]]" = None,
    help: "Optional[str]" = None,
):
    """
    This is partially an alternative to Python 3.9's argparse.BooleanOptionalAction, but this
    function additionally renders help text in a more compact form, while also allowing for
    deprecated identifiers.
    """
    if len(name_or_flags) != 1:
        raise ValueError("can only supply one flag")
    flag = name_or_flags[0]
    if not flag.startswith("--"):
        raise ValueError("flag must start with --")

    base_flag = flag[2:]
    dest = base_flag.replace("-", "_")

    parser.add_argument(
        f"--[no-]{base_flag}",
        help=help,
        nargs=argparse.SUPPRESS,
        action=IgnoreAction,
    )

    parser.add_argument(
        flag,
        help=argparse.SUPPRESS,
        action="store_const",
        const=True,
    )
    parser.add_argument(
        f"--no-{base_flag}",
        help=argparse.SUPPRESS,
        dest=dest,
        action="store_const",
        const=False,
    )
    if hidden_true_flags:
        parser.add_argument(
            *hidden_true_flags,
            help=argparse.SUPPRESS,
            dest=dest,
            action="store_const",
            const=True,
        )


class DashPAction(Action):
    """
    Support for the tricky backwards compatibility game we're playing with the `-p` flag.
    It used to mean ``--party``, but now it means ``--port``.

    Note that Daml-LF defines ``PartyIdString`` as starting with a letter and NEVER with a number,
    so there is no possibility for ambiguity here.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        try:
            port_value = int(values)
            parties_value = None
        except ValueError:
            port_value = None
            parties_value = values.split(",")

        if port_value is not None:
            namespace.port = port_value
        else:
            warnings.warn(
                "-p called with what appears to be a list of parties; use -u instead. "
                "This behavior will be unsupported in dazl v9",
                ConfigWarning,
            )
            existing_parties = getattr(namespace, "act_as", None)
            if existing_parties is None:
                existing_parties = []
                namespace.act_as = existing_parties
            existing_parties.extend(parties_value)


class AppendPartySetAction(Action):
    def __init__(self, option_strings: str, **kwargs):
        super().__init__(option_strings, metavar="PARTY", nargs="+", **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        parties = getattr(namespace, self.dest, None)
        if parties is None:
            parties = []
            setattr(namespace, self.dest, parties)

        parties.extend(party for p in values for party in p.split(","))


class IgnoreAction(Action):
    def __init__(self, warning: Optional[str] = None, *args, **kwargs):
        self.warning = warning
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.warning is not None:
            warnings.warn(self.warning, ConfigWarning)
