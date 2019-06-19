# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains a plugin for capturing data off the ledger and outputting it.
"""

import sys

from functools import partial
from typing import Collection, Iterable, TextIO, Optional, Union, TYPE_CHECKING

from .fmt_base import DEFAULT_FORMATTER_NAME, get_formatter
from .model_capture import LedgerCapture
from ..plugins_base import Plugin
from ...model.core import Party

if TYPE_CHECKING:
    from ...client import LedgerClientManager, Network


class LedgerCapturePlugin(Plugin):
    """
    Plugin that passively listens to the event stream on all parties. Call :meth:`dump_all` to
    render what it sees.
    """

    DEFAULT_FORMATTER_NAME = DEFAULT_FORMATTER_NAME

    @classmethod
    def stdout(cls, **kwargs) -> 'LedgerCapturePlugin':
        """
        Return a :class:`LedgerCapturePlugin` that writes its output to stdout.
        """
        return cls(sys.stdout, False, **kwargs)

    @classmethod
    def stderr(cls, **kwargs) -> 'LedgerCapturePlugin':
        """
        Return a :class:`LedgerCapturePlugin` that writes its output to stderr.
        """
        return cls(sys.stderr, False, **kwargs)

    @classmethod
    def to_file(cls, path, **kwargs) -> 'LedgerCapturePlugin':
        """
        Return a :class:`LedgerCapturePlugin` that writes its output to a file.

        :param path: The file to write to.
        """
        return cls(open(path, 'w'), True, **kwargs)

    def __init__(self,
                 buf: TextIO,
                 buf_close: bool,
                 template_filter: Optional[Iterable[str]]=None,
                 include_archived: bool=False):
        """
        Initialize a :class:`LedgerCapturePlugin`.

        :param buf:
            The buffer to write ledger state to.
        :param buf_close:
            ``True`` to close ``buf`` after fully dumping the contents of the ledger;
            ``False`` to keep ``buf`` open.
        :param template_filter:
            A list of ``str`` of template names. The default value is ``None``, which includes all
            templates.
        :param include_archived:
            ``True`` to include archived contracts in the output;
            otherwise, ``False`` (the default).
        """
        self.buf = buf
        self.buf_close = buf_close
        self.template_filter = template_filter
        self.include_archived = include_archived
        self.manager = None
        self.store = None

    def install(self, manager: 'LedgerClientManager'):
        """
        Monitor the events off of a ledger client.

        :param manager:
            The :class:`LedgerClientManager` to install event handlers into.
        """
        self.manager = manager
        self.manager.on_init_metadata(partial(setattr, self, 'store'))

    def dump_all(self, fmt=None, parties=None, include_archived=None, **kwargs) -> None:
        """
        Write all entries captured by the plugin to the provided buffer.

        :param fmt:
            Format of the output; currently either ``"json"`` or ``"pretty"``.
        :param parties:
            An optional list of parties. If unspecified, the list is taken from the list of parties
            connected to the client.
        :param include_archived:
            ``None`` to use the default value passed in the constructor; ``True`` to include
            archived contracts in the output; otherwise, ``False``.
        :param kwargs:
            Parameters passed directly to the formatter.
        """
        formatter = get_formatter(fmt)

        if self.manager is None:
            lines = formatter.format_error('Plugin not initialized')
        else:
            if parties is None:
                parties = sorted(self.manager.parties())

            include_archived = include_archived if include_archived is not None \
                else self.include_archived

            capture = LedgerCapture()
            capture.store = self.store
            for party in self.manager.parties():
                client = self.manager.client(party)

                if include_archived:
                    for cid, (cdata, state) in client.select('*', include_archived=True).items():
                        if cdata is not None:
                            capture.capture(party, cid, cdata)
                        if not state:
                            capture.capture(party, cid, None)
                else:
                    for cid, cdata in client.select('*').items():
                        capture.capture(party, cid, cdata)

            lines = formatter.format_entries(
                capture=capture,
                parties=parties,
                entries=capture,
                **kwargs)

        for line in lines:
            self.buf.write(line + '\n')


def write_acs(
        buf: 'TextIO',
        network: 'Network',
        fmt: 'Optional[str]' = None,
        parties: 'Collection[Union[str, Party]]' = None,
        include_archived: bool = False,
        **kwargs) \
        -> None:
    """
    Write all entries captured by the plugin to the provided buffer.

    :param buf:
        The buffer to write to.
    :param network:
        The network to write data from.
    :param fmt:
        Format of the output; currently either ``"json"`` or ``"pretty"``.
    :param parties:
        An optional list of parties. If unspecified, the list is taken from the list of parties
        connected to the client.
    :param include_archived:
        ``True`` to include archived contracts in the output; otherwise, ``False``.
    :param kwargs:
        Parameters passed directly to the formatter.
    """
    formatter = get_formatter(fmt)

    if parties is None:
        parties = sorted(network.parties())

    capture = LedgerCapture()
    capture.store = network.simple_global().metadata().store
    for party in parties:
        # TODO: This is a hack because ACS calls on a simple_party instance don't really work once
        #   the loop is closed.
        client = network.aio_party(party)

        for cxdata in client.find_historical('*'):
            if cxdata.active:
                capture.capture(party, cxdata.cid, cxdata.cdata, cxdata.effective_at)
            elif include_archived:
                capture.capture(party, cxdata.cid, None, None)

    lines = formatter.format_entries(
        capture=capture,
        parties=parties,
        entries=capture,
        **kwargs)

    for line in lines:
        buf.write(line + '\n')
