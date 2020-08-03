# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains internal utilities for managing the lifecycle of a process.
"""

import logging
import os
import subprocess
import sys
import time

from datetime import datetime, timedelta
from pathlib import Path
from threading import Thread
from typing import Any, Optional, Sequence, Union


DEFAULT_WATCH_TIMEOUT = timedelta(seconds=10)


class SandboxProcessOptions:
    """
    Information about how to launch a Sandbox.
    """

    def __init__(self, args: 'Sequence[Any]', *,
                 watch_port: 'Optional[int]' = None,
                 watch_timeout: 'Union[None, int, float, timedelta]' = DEFAULT_WATCH_TIMEOUT,
                 logger: 'Optional[logging.Logger]' = None,
                 working_directory: 'Union[None, str, Path]' = None):
        self.args = [str(arg) for arg in args]
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


class SandboxProcessWatcher:
    """
    Manages the lifetime of an external sandbox.
    """
    def __init__(self, process_context: 'SandboxProcessOptions', url: str, sdk_version: str):
        self.process = None
        self.process_context = process_context
        self.logger = self.process_context.logger or logging.getLogger()
        self.url = url
        self.sdk_version = sdk_version

        self._start_entered = False

    def start(self) -> None:
        from ..util.io import is_port_alive

        if self._start_entered:
            return
        self._start_entered = True

        sandbox_env = os.environ.copy()
        if self.sdk_version is not None:
            sandbox_env['DAML_SDK_VERSION'] = self.sdk_version

        self.process = subprocess.Popen(
            self.process_context.args,
            cwd=self.process_context.working_directory,
            env=sandbox_env,
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

    def __enter__(self) -> 'SandboxProcessWatcher':
        self.start()
        return self

    def __exit__(self, typ, value, traceback) -> None:
        self.stop()
