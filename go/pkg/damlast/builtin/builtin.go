package damlast

// classification: builtin

type Unit struct {
}
func (p Parser) ReadUnit(r io.Reader) (v Unit, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		}
	}
}
