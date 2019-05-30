# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import unittest

from dazl.util.io import LoggingStream


class LoggingStreamTest(unittest.TestCase):

    def test_unterminated_write(self):
        logger = MockLogger()
        stream = LoggingStream(logger, None)
        stream.write('abc')
        self.assertEqual(logger.lines, [])

    def test_terminated_write(self):
        logger = MockLogger()
        stream = LoggingStream(logger, None)
        stream.write('abc\n')
        self.assertEqual(['abc'], logger.lines)

    def test_multiple_writes(self):
        logger = MockLogger()
        stream = LoggingStream(logger, None)
        stream.write('abc')
        stream.write('def\n')
        self.assertEqual(['abcdef'], logger.lines)

    def test_multiple_writes_of_lines(self):
        logger = MockLogger()
        stream = LoggingStream(logger, None)
        stream.write('abc\n')
        stream.write('def\n')
        self.assertEqual(['abc', 'def'], logger.lines)

    def test_multiple_writelines(self):
        logger = MockLogger()
        stream = LoggingStream(logger, None)
        stream.write('abc')
        stream.writelines(['def', 'ghi'])
        stream.write('jkl\n')
        self.assertEqual(['abcdef', 'ghi', 'jkl'], logger.lines)

    def test_complex(self):
        logger = MockLogger()
        stream = LoggingStream(logger, None)
        stream.write('abc')
        stream.write('def\nghi\njkl')
        stream.write('mno')
        stream.write('\n')
        self.assertEqual(['abcdef', 'ghi', 'jklmno'], logger.lines)


class MockLogger:

    def __init__(self):
        self.lines = []

    def log(self, log_level, message, *args, **kwargs):
        self.lines.append(message)
