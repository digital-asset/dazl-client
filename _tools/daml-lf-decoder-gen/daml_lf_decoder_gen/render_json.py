import json
from dataclasses import asdict

from . import adt


def render_json(package: adt.Package):
    print(json.dumps(asdict(package), indent='  '))
