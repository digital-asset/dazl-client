from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_metadata_filter import PackageMetadataFilter
    from ..models.topology_state_filter import TopologyStateFilter


T = TypeVar("T", bound="ListVettedPackagesRequest")


@_attrs_define
class ListVettedPackagesRequest:
    """
    Attributes:
        page_token (str): Pagination token to determine the specific page to fetch. Using the token
            guarantees that ``VettedPackages`` on a subsequent page are all greater
            (``VettedPackages`` are sorted by synchronizer ID then participant ID) than
            the last ``VettedPackages`` on a previous page.

            The server does not store intermediate results between calls chained by a
            series of page tokens. As a consequence, if new vetted packages are being
            added and a page is requested twice using the same token, more packages can
            be returned on the second call.

            Leave unspecified (i.e. as empty string) to fetch the first page.

            Optional
        page_size (int): Maximum number of ``VettedPackages`` results to return in a single page.

            If the page_size is unspecified (i.e. left as 0), the server will decide
            the number of results to be returned.

            If the page_size exceeds the maximum supported by the server, an
            error will be returned.

            To obtain the server's maximum consult the PackageService descriptor
            available in the VersionService.

            Optional
        package_metadata_filter (PackageMetadataFilter | Unset): Filter the VettedPackages by package metadata.

            A PackageMetadataFilter without package_ids and without package_name_prefixes
            matches any vetted package.

            Non-empty fields specify candidate values of which at least one must match.
            If both fields are set, then a candidate is returned if it matches one of the fields.
        topology_state_filter (TopologyStateFilter | Unset): Filter the vetted packages by the participant and
            synchronizer that they are
            hosted on.

            Empty fields are ignored, such that a ``TopologyStateFilter`` without
            participant_ids and without synchronizer_ids matches a vetted package hosted
            on any participant and synchronizer.

            Non-empty fields specify candidate values of which at least one must match.
            If both fields are set then at least one candidate value must match from each
            field.
    """

    page_token: str
    page_size: int
    package_metadata_filter: PackageMetadataFilter | Unset = UNSET
    topology_state_filter: TopologyStateFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_token = self.page_token

        page_size = self.page_size

        package_metadata_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_metadata_filter, Unset):
            package_metadata_filter = self.package_metadata_filter.to_dict()

        topology_state_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.topology_state_filter, Unset):
            topology_state_filter = self.topology_state_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageToken": page_token,
                "pageSize": page_size,
            }
        )
        if package_metadata_filter is not UNSET:
            field_dict["packageMetadataFilter"] = package_metadata_filter
        if topology_state_filter is not UNSET:
            field_dict["topologyStateFilter"] = topology_state_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_metadata_filter import PackageMetadataFilter
        from ..models.topology_state_filter import TopologyStateFilter

        d = dict(src_dict)
        page_token = d.pop("pageToken")

        page_size = d.pop("pageSize")

        _package_metadata_filter = d.pop("packageMetadataFilter", UNSET)
        package_metadata_filter: PackageMetadataFilter | Unset
        if isinstance(_package_metadata_filter, Unset):
            package_metadata_filter = UNSET
        else:
            package_metadata_filter = PackageMetadataFilter.from_dict(_package_metadata_filter)

        _topology_state_filter = d.pop("topologyStateFilter", UNSET)
        topology_state_filter: TopologyStateFilter | Unset
        if isinstance(_topology_state_filter, Unset):
            topology_state_filter = UNSET
        else:
            topology_state_filter = TopologyStateFilter.from_dict(_topology_state_filter)

        list_vetted_packages_request = cls(
            page_token=page_token,
            page_size=page_size,
            package_metadata_filter=package_metadata_filter,
            topology_state_filter=topology_state_filter,
        )

        list_vetted_packages_request.additional_properties = d
        return list_vetted_packages_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
