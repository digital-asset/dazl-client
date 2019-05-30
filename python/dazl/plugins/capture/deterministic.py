# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities for deterministically outputting contract information.
"""

from collections import defaultdict


def collate_entries(metadata, parties, entries):
    """
    Return entries as a dict of :class:`TemplateMetadata` to list of :class:`LedgerCaptureEntry`.
    """
    sort = EntrySorter(parties)

    entries_by_template = defaultdict(list)
    for entry in entries:
        entries_by_template[entry.template_id].append(entry)

    grouped_entries = []
    for template_id, entries in entries_by_template.items():
        template = metadata.templates.find(template_id)
        entries.sort(key=sort.key)
        grouped_entries.append((template, entries))

    grouped_entries.sort(key=lambda t: t[0].template_name)
    return dict(grouped_entries)


class EntrySorter:
    """
    Implementation of a sort key method for :class:`LedgerCaptureEntry`.
    """
    def __init__(self, parties):
        self.parties = parties

    def key(self, entry):
        """
        Return an expression that can be used as an absolute sorting value as a proxy for this
        entry.
        """
        party_vis = [1 if entry.parties.get(party) is not None else 0 for party in self.parties]
        return sum(party_vis), ''.join(map(str, reversed(party_vis)))
