from asyncio import ensure_future, new_event_loop, set_event_loop, sleep, gather
from pathlib import Path
from unittest import TestCase

from dazl import Network, sandbox
from dazl.util.dar import TemporaryDar


DAML_FILE = Path(__file__).parent.parent / 'resources' / 'AllKindsOf.daml'


class TestDarUpload(TestCase):
    def test_dar_uploads_near_startup(self):
        set_event_loop(new_event_loop())

        package_ids = []

        async def upload_dars_and_verify():
            g = network.aio_global()
            await gather(*[ensure_future(g.ensure_dar(file.read_bytes())) for file in dar_files])

            metadata = await g.metadata()
            package_ids.extend(metadata.store.package_ids())

        with sandbox([]) as proc, TemporaryDar(DAML_FILE) as dar_files:
            network = Network()
            network.set_config(url=proc.url)
            network.run_until_complete(upload_dars_and_verify())

        self.assertGreater(len(package_ids), 0)

