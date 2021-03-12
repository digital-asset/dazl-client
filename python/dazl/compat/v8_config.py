from typing import Any, Dict

from ..protocols.config import Config


class NetworkConfig:
    def __init__(self):
        self._config = dict()  # type: Dict[str, Any]

    def new_style_config(self) -> "Config":
        return Config.create(**self._config)
