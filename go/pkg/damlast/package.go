//package damlast
//
//
//type Package struct {
//	metadata *PackageMetadata
//	modules []Module
//}
//
//func NewPackage(metadata *PackageMetadata, modules []Module) *Package {
//	return &Package{
//		metadata: metadata,
//		modules: modules,
//	}
//}
//
//func (p *Package) Metadata() *PackageMetadata {
//	return p.metadata
//}
//
//func NewPackageMetadata(name string, version string) *PackageMetadata {
//	return &PackageMetadata{
//		name: name,
//		version: version,
//	}
//}
//
//type PackageMetadata struct {
//	name string
//	version string
//}
//
//func (pm *PackageMetadata) Name() string {
//	if pm == nil {
//		return ""
//	}
//	return pm.name
//}
//
//func (pm *PackageMetadata) Version() string {
//	if pm == nil {
//		return ""
//	}
//	return pm.version
//}
//
//type Module struct {
//	name string
//	synonyms []DefTypeSyn
//	dataTypes []DefDataType
//	values []DefValue
//	templates []DefTemplate
//}
//
//type DefTypeSyn struct {
//	name string
//	params []TypeVarWithKind
//	type_ Type
//	location Location
//}
//
//func NewDefTypeSyn(name string, params []TypeVarWithKind, type_ Type, location Location) DefTypeSyn {
//	if params == nil {
//		params = []TypeVarWithKind{}
//	}
//
//	return DefTypeSyn{
//		name:     name,
//		params:   nil,
//		type_:    type_,
//		location: location,
//	}
//}
//
//type TypeVarWithKind struct {
//
//}
//
//type Location struct {
//
//}
