# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Internal module used by dazl's build process to generate files from Protobuf/gRPC definitions.

**This is not a public API and its implementation details are subject to change at any time!**

The generated code was lightly inspired by https://github.com/dropbox/mypy-protobuf.
Its output differs in some key ways:

 * `mypy-protobuf` 's stubs are not (yet) compatible with the gRPC asyncio library.
 * Protobuf symbols (message names, enum values, service names, etc) are not allowed to start with
   underscores; as much as possible, we try to use underscore prefixes before all of our symbols
   (see `Protobuf Spec <https://developers.google.com/protocol-buffers/docs/reference/proto3-spec>`_).
"""
