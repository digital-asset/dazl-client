package damlast

// classification: lf

type Archive struct {
	hash PackageRef
	pkg Package
}
func (p Parser) ReadArchive(r io.Reader) (v Archive, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 4: // hash
			v.hash, err = p.ReadPackageRef(r)
		case 3: // package
			v.pkg, err = p.ReadPackage(r)
		}
	}
}
