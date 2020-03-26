package grpc

type LedgerApiValuer interface {
	LedgerApiValue() (lapi.Value, error)
}

type ledgerApiValuerWrapper struct {
	theType context
	value interface{}
}






