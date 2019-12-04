from pathlib import Path
from unittest import TestCase

from dazl import LOG, setup_default_logger

import logging
from dazl.util.dar import DarFile

ARCHIVES: Path = Path(__file__).absolute().parent.parent.parent.parent / '_fixtures' / 'archives'
setup_default_logger(logging.DEBUG)


class TestHistoricalDarParsing(TestCase):
    def test_dar_version_compatibility(self):
        dars = list(ARCHIVES.glob('**/*.dar'))
        self.assertGreater(len(dars), 0, f'Could not find any DARs in {ARCHIVES}')

        for dar in ARCHIVES.glob('**/*.dar'):
            short_dar = dar.relative_to(ARCHIVES)
            with self.subTest(str(short_dar)):
                dar_file = DarFile(dar)
                metadata = dar_file.read_metadata()
                LOG.info('Successfully read %s with package IDs %r.', short_dar,
                         metadata.package_ids())

