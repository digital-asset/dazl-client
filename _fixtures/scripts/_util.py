from typing import NamedTuple


class SdkVersion(NamedTuple):
    @classmethod
    def parse(cls, s: str) -> 'Optional[SdkVersion]':
        # allow the version string to start with a leading 'v', which we strip
        # out
        if s.startswith('v'):
            s = s[1:]

        try:
            components = s.split('.')
            return cls(*map(int, components))
        except ValueError:
            return None
        

    major: int
    minor: int
    patch: int

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'
