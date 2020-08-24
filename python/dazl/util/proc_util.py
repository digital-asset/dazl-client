# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import sys
import time
from datetime import datetime
from subprocess import Popen, TimeoutExpired
from threading import Event, Thread
from .prim_types import TimeDeltaConvertible, to_timedelta


def kill_process_tree(process: 'Popen'):
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
        logging.error(
            'Had trouble killing a sandbox process normally; it will be forcibly killed.')
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


def wait_for_process_port(process: 'Popen', port: int, timeout: 'TimeDeltaConvertible') -> None:
    from ..model.core import ProcessDiedException
    from .io import is_port_alive

    alive = False
    max_time_wait = datetime.utcnow() + to_timedelta(timeout)

    logging.debug('Waiting for port %s to be alive on pid %s...', port, process.pid)
    while (max_time_wait is None or (datetime.utcnow() < max_time_wait)) \
            and process.poll() is None and not alive:
        alive = is_port_alive(port)
        if not alive:
            time.sleep(0.1)

    if not alive:
        return_code = process.returncode
        if return_code is not None:
            raise ProcessDiedException(return_code, 'The process exited with an error code')
        raise Exception('Timed out while waiting for a process to start')


class ProcessLogger:
    """
    Pipe stdout and stderr from a process to the logger.
    """

    def __init__(self, process: 'Popen', logger: 'logging.Logger'):
        self.process = process
        self.logger = logger
        self._evt = Event()

    def start(self):
        stdout = sys.stdout
        stderr = sys.stderr
        stdout_log_thread = Thread(target=self._stdout_monitor, args=[stdout])
        stdout_log_thread.start()
        stderr_log_thread = Thread(target=self._stderr_monitor, args=[stderr])
        stderr_log_thread.start()

    def stop(self):
        self._evt.set()

    def _stdout_monitor(self, stdout):
        sys.stdout = stdout
        # noinspection PyBroadException
        try:
            for line in self.process.stdout:
                if self._evt.is_set():
                    return

                self.logger.info(line.rstrip('\n'))
        except:  # noqa
            pass

    def _stderr_monitor(self, stderr):
        sys.stderr = stderr
        # noinspection PyBroadException
        try:
            for line in self.process.stderr:
                if self._evt.is_set():
                    return

                self.logger.info(line.rstrip('\n'))
        except:  # noqa
            pass
