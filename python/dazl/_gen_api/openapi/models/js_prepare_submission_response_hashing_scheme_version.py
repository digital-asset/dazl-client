from enum import Enum


class JsPrepareSubmissionResponseHashingSchemeVersion(str, Enum):
    HASHING_SCHEME_VERSION_UNSPECIFIED = "HASHING_SCHEME_VERSION_UNSPECIFIED"
    HASHING_SCHEME_VERSION_V2 = "HASHING_SCHEME_VERSION_V2"

    def __str__(self) -> str:
        return str(self.value)
