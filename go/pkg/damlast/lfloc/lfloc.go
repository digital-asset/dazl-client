package damlast

// classification: lfloc

type Location struct {
	module ModuleRef
	rng Location_Range
}
func (p Parser) ReadLocation(r io.Reader) (v Location, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // module
			v.module, err = p.ReadModuleRef(r)
		case 2: // range
			v.rng, err = p.ReadLocation_Range(r)
		}
	}
}
// classification: lfloc

type Location_Range struct {
	startLine int32
	startCol int32
	endLine int32
	endCol int32
}
func (p Parser) ReadLocation_Range(r io.Reader) (v Location_Range, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // start_line
			v.startLine, err = p.Readint32(r)
		case 2: // start_col
			v.startCol, err = p.Readint32(r)
		case 3: // end_line
			v.endLine, err = p.Readint32(r)
		case 4: // end_col
			v.endCol, err = p.Readint32(r)
		}
	}
}
