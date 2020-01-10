# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from dazl.util.io import LoggingStream


def test_unterminated_write():
    logger = MockLogger()
    stream = LoggingStream(logger, None)
    stream.write('abc')
    assert [] == logger.lines


def test_terminated_write():
    logger = MockLogger()
    stream = LoggingStream(logger, None)
    stream.write('abc\n')
    assert ['abc'] == logger.lines


def test_multiple_writes():
    logger = MockLogger()
    stream = LoggingStream(logger, None)
    stream.write('abc')
    stream.write('def\n')
    assert ['abcdef'] == logger.lines


def test_multiple_writes_of_lines():
    logger = MockLogger()
    stream = LoggingStream(logger, None)
    stream.write('abc\n')
    stream.write('def\n')
    assert ['abc', 'def'] == logger.lines


def test_multiple_writelines():
    logger = MockLogger()
    stream = LoggingStream(logger, None)
    stream.write('abc')
    stream.writelines(['def', 'ghi'])
    stream.write('jkl\n')
    assert ['abcdef', 'ghi', 'jkl'] == logger.lines


def test_complex():
    logger = MockLogger()
    stream = LoggingStream(logger, None)
    stream.write('abc')
    stream.write('def\nghi\njkl')
    stream.write('mno')
    stream.write('\n')
    assert ['abcdef', 'ghi', 'jklmno'] == logger.lines


class MockLogger:

    def __init__(self):
        self.lines = []

    def log(self, log_level, message, *args, **kwargs):
        self.lines.append(message)
