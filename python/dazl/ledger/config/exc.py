__all__ = ["ConfigError", "ConfigWarning"]


class ConfigError(ValueError):
    pass


class ConfigWarning(Warning):
    pass
