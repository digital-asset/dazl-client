# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from http.server import HTTPServer
from threading import Thread


class TestHTTPServer:
    """
    Runner for an HTTP server in a background thread.
    """

    def __init__(self, handler, port=0):
        self._thread = Thread(target=self._run)
        self.server = HTTPServer(("localhost", port), handler)

    @property
    def port(self):
        return self.server.server_port

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.shutdown()
        self._thread.join()

    def _run(self):
        self.server.serve_forever()
        self.server.socket.close()
