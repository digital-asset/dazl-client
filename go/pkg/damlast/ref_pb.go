package damlast

import (
	pb "github.com/digital-asset/dazl/go/gen/com/daml/daml_lf_dev"
	"strings"
)

type DecodeContext struct {
	self PackageRef
}

func NewPackageParseContext(message *pb.Package, self PackageRef) (*DecodeContext, error) {
	return &DecodeContext{
		self: self,
	}
}

func (*DecodeContext) InternedDottedName(i int32) DottedName {
	return self
}

func (*DecodeContext) ParseError(err string) error {

}


func DecodeDottedName(_ *DecodeContext, message *pb.DottedName) (DottedName, error) {
	return DottedName(strings.Join(message.Segments, ".")), nil
}

func DecodePackage(ctx *DecodeContext, message *pb.Package) (Package, error) {
	metadata, err := DecodePackageMetadata(ctx, message.Metadata)
	if err != nil {
		return nil, err
	}

	modules := []Module
	for _, moduleMessage := range message.Modules {
		module, err := DecodeModule(message)
		if err != nil {
			return nil, err
		}
		modules = append(modules, module)
	}

	return NewPackage(metadata, modules), nil
}
