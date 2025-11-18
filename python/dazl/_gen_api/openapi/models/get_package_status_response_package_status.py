from enum import Enum


class GetPackageStatusResponsePackageStatus(str, Enum):
    PACKAGE_STATUS_REGISTERED = "PACKAGE_STATUS_REGISTERED"
    PACKAGE_STATUS_UNSPECIFIED = "PACKAGE_STATUS_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
