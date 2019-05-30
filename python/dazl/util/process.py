# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains internal utilities for managing the lifecycle of a process.
"""

import logging
import subprocess
import sys
import time

from datetime import datetime, timedelta
from pathlib import Path
from threading import Thread
from typing import Any, ContextManager, Optional, Sequence, Union

from .io import is_port_alive


DEFAULT_WATCH_TIMEOUT = timedelta(seconds=10)


class ProcessContext:
    """
    Information about how to launch a process, and a context manager that optionally manages
    any temporary resources that need to be kept around while the process is running.
    """

    def __init__(self, args: 'Sequence[Any]', *,
                 secondary_context: 'Optional[ContextManager]' = None,
                 watch_port: 'Optional[int]' = None,
                 watch_timeout: 'Union[None, int, float, timedelta]' = DEFAULT_WATCH_TIMEOUT,
                 logger: 'Optional[logging.Logger]' = None,
                 working_directory: 'Union[None, str, Path]' = None,
                 extra_data: 'Optional[dict]' = None):
        self.args = [str(arg) for arg in args]
        self.secondary_context = secondary_context
        self.watch_port = watch_port

        if isinstance(watch_timeout, (int, float)):
            self.watch_timeout = timedelta(seconds=watch_timeout)
        elif isinstance(watch_timeout, timedelta):
            self.watch_timeout = watch_timeout
        elif watch_timeout is None:
            self.watch_timeout = None
        else:
            raise TypeError(f'Not a valid watch timeout: {watch_timeout!r}')

        self.watch_timeout = watch_timeout
        self.logger = logger

        if isinstance(working_directory, Path):
            self.working_directory = str(working_directory)
        elif isinstance(working_directory, str):
            self.working_directory = working_directory
        elif working_directory is None:
            self.working_directory = None
        else:
            raise TypeError(f'Not a valid working directory: {working_directory!r}')

        self.extra_data = extra_data or {}

    def __enter__(self):
        if self.secondary_context is not None:
            self.secondary_context.__enter__()
        return self.args

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.secondary_context is not None:
            self.secondary_context.__exit__(exc_type, exc_val, exc_tb)


class ProcessWatcher:
    """
    Manages the lifetime of an external process.
    """
    def __init__(self, process_context: 'ProcessContext'):
        self.process = None
        self.process_context = process_context
        self.logger = self.process_context.logger or logging.getLogger()

        self._start_entered = False

    def start(self) -> None:
        if self._start_entered:
            return
        self._start_entered = True

        self.process_context.__enter__()
        self.process = subprocess.Popen(
            self.process_context.args,
            cwd=self.process_context.working_directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True)

        stdout = sys.stdout
        stderr = sys.stderr
        stdout_log_thread = Thread(target=self._stdout_monitor, args=[stdout])
        stdout_log_thread.start()
        stderr_log_thread = Thread(target=self._stderr_monitor, args=[stderr])
        stderr_log_thread.start()

        port = self.process_context.watch_port
        if port is None:
            return

        alive = False
        if self.process_context.watch_timeout is not None:
            max_time_wait = datetime.utcnow() + self.process_context.watch_timeout
        else:
            max_time_wait = None

        logging.debug('Waiting for port %s to be alive on pid %s...', port, self.process.pid)
        while ((max_time_wait is None or datetime.utcnow() < max_time_wait) and
               self.process.poll() is None and not alive):
            alive = is_port_alive(port)
            if not alive:
                time.sleep(0.1)
        if not alive:
            return_code = self.process.returncode
            if return_code is not None:
                from ..model.core import ProcessDiedException
                raise ProcessDiedException(return_code, 'The sandbox exited with an error code')
            raise Exception('Timed out while waiting for the sandbox to start')

    def stop(self) -> None:
        if self.process is not None:
            try:
                import psutil
                children = psutil.Process(pid=self.process.pid).children()
                logging.info('Child processes: %s', children)
            except:
                children = []

            self.process.terminate()
            try:
                # give the process two seconds to die
                self.process.communicate(timeout=5)

            except subprocess.TimeoutExpired:
                logging.error('Had trouble killing a sandbox process normally; '
                              'it will be forcibly killed.')
                # if there are child processes, start working around the parent process and try to
                # terminate them directly
                for child in children:
                    try:
                        child.kill()
                    except:
                        pass

                self.process.kill()
                self.process.communicate()
            self.process = None
        if self.process_context is not None:
            self.process_context.__exit__(None, None, None)
            self.process_context = None

    def run(self) -> int:
        """
        Run the process to completion.
        """
        self.start()
        self.process.wait()
        return self.process.returncode

    def _stdout_monitor(self, stdout):
        sys.stdout = stdout
        # noinspection PyBroadException
        try:
            for line in self.process.stdout:
                self.logger.info(line.rstrip('\n'))
        except:  # noqa
            pass

    def _stderr_monitor(self, stderr):
        sys.stderr = stderr
        # noinspection PyBroadException
        try:
            for line in self.process.stderr:
                # TODO: Make this configurable; happens to be that our tools currently print things
                # to stderr that probably better belong on stdout
                self.logger.info(line.rstrip('\n'))
        except:  # noqa
            pass

    def __enter__(self) -> 'ProcessWatcher':
        self.start()
        return self

    def __exit__(self, typ, value, traceback) -> None:
        self.stop()
