package damlast


type PackageRef string
type DottedName string
type ModuleRef string
type Unit struct {}


type Package interface {
	Metadata() PackageMetadata
	Modules() []Module
}


type packageImpl struct {
	metadata PackageMetadata
}


func (impl packageImpl) Metadata() PackageMetadata {
	return impl.metadata
}


func NewPackageRef() PackageRef {

}