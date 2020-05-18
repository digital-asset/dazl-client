# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


DEFAULT_FORMATTER_NAME = 'pretty'


def get_formatter(fmt):
    """
    Return a formatter of the specified name.
    """
    if fmt is None:
        fmt = DEFAULT_FORMATTER_NAME

    if fmt == 'json':
        from . import fmt_json
        return fmt_json
    elif fmt == 'pretty':
        from . import fmt_pretty
        return fmt_pretty
    else:
        raise ValueError('unknown format: {}'.format(fmt))
