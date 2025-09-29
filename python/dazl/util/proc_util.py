# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from contextlib import ExitStack
from datetime import datetime
import logging
from os import PathLike
from pathlib import Path
from subprocess import Popen, TimeoutExpired
import sys
from threading import Event, Thread
import time
from typing import Optional, TextIO

from google.protobuf.empty_pb2 import Empty
from grpc import insecure_channel, secure_channel, ssl_channel_credentials

from .._gen.com.digitalasset.canton.health.admin.v0.status_service_pb2_grpc import StatusServiceStub
from ..prim import DazlError, TimeDeltaLike, to_timedelta

__all__ = ["kill_process_tree", "wait_for_process_port", "ProcessLogger", "ProcessDiedException"]


def kill_process_tree(process: Popen) -> None:
    """
    Kill a process and its children.
    """
    #
    # noinspection PyBroadException
    try:
        # noinspection PyPackageRequirements,PyUnresolvedReferences
        import psutil

        children = psutil.Process(pid=process.pid).children()
    except:  # noqa
        children = []

    process.terminate()
    try:
        # give the process a few seconds to die
        process.communicate(timeout=5)

    except TimeoutExpired:
        logging.error("Had trouble killing a sandbox process normally; it will be forcibly killed.")
        # if there are child processes, start working around the parent process and try to
        # terminate them directly
        #
        # noinspection PyBroadException
        for child in children:
            try:
                child.kill()
            except:  # noqa
                pass

        process.kill()
        process.communicate()


def wait_for_process_port(
    process: Popen,
    port: int,
    timeout: TimeDeltaLike,
    *,
    participant_admin_port: Optional[int] = None,
    participant_admin_cert_file: Optional[PathLike] = None,
) -> None:
    from .io import is_port_alive

    alive = False
    max_time_wait = datetime.utcnow() + to_timedelta(timeout)

    logging.debug("Waiting for port %s to be alive on pid %s...", port, process.pid)
    while (
        (max_time_wait is None or (datetime.utcnow() < max_time_wait))
        and process.poll() is None
        and not alive
    ):
        alive = is_port_alive(port)
        if alive:
            # additionally check for an active participant_admin_port and only do a status check
            # if that port is open
            if participant_admin_port is not None and is_port_alive(participant_admin_port):
                logging.debug("Waiting for the participant to report itself as active...")
                with ExitStack() as stack:
                    if participant_admin_cert_file is not None:
                        credentials = ssl_channel_credentials(
                            root_certificates=Path(participant_admin_cert_file).read_bytes()
                        )
                        channel = stack.enter_context(
                            secure_channel(f"localhost:{participant_admin_port}", credentials)
                        )
                    else:
                        channel = stack.enter_context(
                            insecure_channel(f"localhost:{participant_admin_port}")
                        )
                    status_service = StatusServiceStub(channel)
                    response = status_service.Status(Empty())
                    alive = response.success.active

                if not alive:
                    time.sleep(0.5)

    if not alive:
        return_code = process.returncode
        if return_code is not None:
            raise ProcessDiedException(return_code, "The process exited with an error code")
        raise Exception("Timed out while waiting for a process to start")


class ProcessLogger:
    """
    Pipe stdout and stderr from a process to the logger.
    """

    def __init__(self, process: Popen, logger: logging.Logger) -> None:
        self.process = process
        self.logger = logger
        self._evt = Event()

    def start(self) -> None:
        stdout = sys.stdout
        stderr = sys.stderr
        stdout_log_thread = Thread(target=self._stdout_monitor, args=[stdout])
        stdout_log_thread.start()
        stderr_log_thread = Thread(target=self._stderr_monitor, args=[stderr])
        stderr_log_thread.start()

    def stop(self) -> None:
        self._evt.set()

    def _stdout_monitor(self, stdout: TextIO) -> None:
        sys.stdout = stdout
        # noinspection PyBroadException
        try:
            proc_stdout = self.process.stdout
            if proc_stdout is not None:
                for line in proc_stdout:
                    if self._evt.is_set():
                        return

                    self.logger.info(line.rstrip("\n"))
        except:  # noqa
            pass

    def _stderr_monitor(self, stderr: TextIO) -> None:
        sys.stderr = stderr
        # noinspection PyBroadException
        try:
            proc_stderr = self.process.stderr
            if proc_stderr is not None:
                for line in proc_stderr:
                    if self._evt.is_set():
                        return

                    self.logger.info(line.rstrip("\n"))
        except:  # noqa
            pass


class ProcessDiedException(DazlError):
    pass
