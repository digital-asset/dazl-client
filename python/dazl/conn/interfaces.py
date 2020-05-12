# Copyright (c) 2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


class LedgerConnectionPool:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self, url: str, auth_token, party):
        raise NotImplementedError('LedgerConnectionPool.connect not implemented')

    def close(self):
        raise NotImplementedError('LedgerConnectionPool.close not implemented')


class LedgerConnection:
    """
    Base class for ledger connections.
    """

    def submit(self, command):
        """
        Submit a set of commands to the ledger.
        """
        raise NotImplementedError('LedgerConnection.submit not implemented')

    def submit_create(self, command):
        """
        Submit a single create command to the ledger, and return the resulting CreatedEvent.
        """
        raise NotImplementedError('LedgerConnection.submit_create not implemented')

    def submit_create_and_exercise(self, command):
        """
        Submit a single create-and-exercise command to the ledger, and return the resulting
        ExercisedEvent.
        """
        raise NotImplementedError('LedgerConnection.submit_create_and_exercise not implemented')

    def submit_exercise(self, command):
        """
        Submit a single exercise command to the ledger, and return the resulting ExercisedEvent.
        """
        raise NotImplementedError('LedgerConnection.submit_exercise not implemented')

    def submit_exercise_by_key(self, command):
        """
        Submit a single exercise-by-key command to the ledger, and return the resulting
        ExercisedEvent.
        """
        raise NotImplementedError('LedgerConnection.submit_exercise_by_key not implemented')

    def query(self, query):
        """
        Return a stream of transactions.
        """
        raise NotImplementedError('LedgerConnection.query not implemented')

    def fetch_acs(self, template_ids):
        """
        Return the ACS for the specified set of template IDs.
        """
        raise NotImplementedError('LedgerConnection.fetch_acs not implemented')

    def fetch_package_ids(self):
        """
        Return the set of package IDs on the ledger.
        """
        raise NotImplementedError('LedgerConnection.fetch_package_ids not implemented')

    def fetch_package_bytes(self, package_id):
        """
        Return the bytes for the package ref.
        """
        raise NotImplementedError('LedgerConnection.fetch_package_bytes not implemented')

    def upload_package_bytes(self, contents):
        """
        Upload a package.
        """
        raise NotImplementedError('LedgerConnection.upload_package_bytes not implemented')

    def close(self):
        """
        Close the underlying connection.
        """


class AsyncLedgerConnection(LedgerConnection):
    """
    The :class:`LedgerConnection` protocol defines protocol/transport-specific implementations of
    common ledger operations implemented using blocking semantics. These loosely correlate to the
    current set of gRPC Ledger API and HTTP-JSON API services.
    """


class BlockingLedgerConnection(LedgerConnection):
    """
    The :class:`LedgerConnection` protocol defines protocol/transport-specific implementations of
    common ledger operations implemented using blocking semantics. These loosely correlate to the
    current set of gRPC Ledger API and HTTP-JSON API services.
    """
