from unittest import TestCase


class TestJsonSerialize(TestCase):

    def test_serializers(self):
        # merely import the SCALAR_FORMATTERS symbol, which runs a check to make sure that all
        # scalars can be safely serialized in JSON
        from dazl.protocols.v0.json_ser_command import _SCALAR_FORMATTERS
        self.assertIsNotNone(_SCALAR_FORMATTERS)
