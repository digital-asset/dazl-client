package damlast

import (
	"testing"
)

func  Test(t *testing.T) {
	a := NewArchive(PackageRef(""), NewPackage())
	a.Package().
	NewType(NewTypeVar("a", nil))

	Ledger{}.Archive().Do(ctx, conn)
}
