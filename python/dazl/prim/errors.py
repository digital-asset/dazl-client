# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


__all__ = ["DazlError", "DazlWarning", "DazlImportError"]

import warnings


class DazlError(Exception):
    """
    Superclass of errors raised by dazl.
    """


class DazlWarning(Warning):
    """
    Superclass of warnings raised by dazl.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            "DazlWarning is deprecated; it and UnknownTemplateWarning wil be removed in dazl v9",
            DeprecationWarning,
            stacklevel=2,
        )


class DazlImportError(ImportError, DazlError):
    """
    Import error raised when an optional dependency could not be found.
    """

    def __init__(self, missing_module, message):
        super().__init__(message)
        warnings.warn(
            "DazlImportError will be removed in dazl v9; prefer to catch ImportError instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self.missing_module = missing_module
