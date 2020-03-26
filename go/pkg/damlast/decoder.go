package damlast

import (
	pb "github.com/digital-asset/dazl/go/gen/com/daml/daml_lf_dev"
	"github.com/golang/protobuf/proto"

)

func Decode(archive []byte) (*Package, error) {
	var payload daml_lf_dev.ArchivePayload
	if err := proto.Unmarshal(archive, &payload); err != nil {
		return nil, err
	}
	return DecodeV1(payload.GetDamlLf_1())
}

func DecodeV1(packageId string, p *pb.Package) (*Package, error) {
	var errors []error
	var parser = parser{
		packageId: packageId,
		errors:    &errors,
	}

	var modules []Module
	p.GetMetadata()
	metadata, err1 := parser.ParseMetadata(p.Metadata)
	for _, m := range p.Modules {
		module, err := parser.ParseModule(m)
		if err != nil {
			errors = append(errors, err)
		}
		if module != nil {
			modules = append(modules, *module)
		}
	}

	if err1 != nil {
		return nil, NewParseError(".", err1)
	}

	return NewPackage(metadata, modules), nil
}

func (parser *parser) ParseMetadata(metadata *pb.PackageMetadata) (*PackageMetadata, error) {
	if metadata == nil {
		return nil, nil
	}

	name, err1 := parser.String(metadata.NameInternedStr)
	version, err2 := parser.String(metadata.VersionInternedStr)

	if err1 != nil || err2 != nil {
		return nil, NewParseError("metadata", err1, err2)
	}

	return NewPackageMetadata(name, version), nil
}

func (parser *parser) ParseModule(module *pb.Module) (*Module, error) {
	module.
}

type parser struct {
	packageId string
	errors *[]error
	intern
}

func (*parser) String(id int32) (string, error) {
	return parser.
}