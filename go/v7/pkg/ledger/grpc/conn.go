package grpc

import (
	"context"
)

type connection struct {
}
func (c* connection) Create(ctx context.Context, create CreateCommand, opts ...CommandOpts) (CreateEvent, error) {
	request := lapipb.SubmitAndWaitRequest{
		Commands: lapipb.Commands{
		},
	}

	response, err := stub.SubmitAndWaitForTransaction()
	if err != nil {
	}

	return c.codec.DecodeCreatedEvent(response.Transaction.Events[0].Created)
}

func (c*connection) Exercise(ctx context.Context, exercise ExerciseCommand, opts...CommandOpts) (ExerciseResult, error) {

}