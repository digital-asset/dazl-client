from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.map_string import MapString


T = TypeVar("T", bound="ObjectMeta")


@_attrs_define
class ObjectMeta:
    """Represents metadata corresponding to a participant resource (e.g. a participant user or participant local
    information about a party).

    Based on ``ObjectMeta`` meta used in Kubernetes API.
    See https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/generated.proto#L640

        Attributes:
            resource_version (str): An opaque, non-empty value, populated by a participant server which represents the
                internal version of the resource
                this ``ObjectMeta`` message is attached to. The participant server will change it to a unique value each time
                the corresponding resource is updated.
                You must not rely on the format of resource version. The participant server might change it without notice.
                You can obtain the newest resource version value by issuing a read request.
                You may use it for concurrent change detection by passing it back unmodified in an update request.
                The participant server will then compare the passed value with the value maintained by the system to determine
                if any other updates took place since you had read the resource version.
                Upon a successful update you are guaranteed that no other update took place during your read-modify-write
                sequence.
                However, if another update took place during your read-modify-write sequence then your update will fail with an
                appropriate error.
                Concurrent change control is optional. It will be applied only if you include a resource version in an update
                request.
                When creating a new instance of a resource you must leave the resource version empty.
                Its value will be populated by the participant server upon successful resource creation.
                Optional
            annotations (MapString):
    """

    resource_version: str
    annotations: MapString
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_version = self.resource_version

        annotations = self.annotations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceVersion": resource_version,
                "annotations": annotations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_string import MapString

        d = dict(src_dict)
        resource_version = d.pop("resourceVersion")

        annotations = MapString.from_dict(d.pop("annotations"))

        object_meta = cls(
            resource_version=resource_version,
            annotations=annotations,
        )

        object_meta.additional_properties = d
        return object_meta

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
