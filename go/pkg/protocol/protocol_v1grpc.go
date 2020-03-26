package protocol

import (
	"context"
	"errors"
	"fmt"
	v1 "github.com/digital-asset/dazl/go/gen/com/daml/ledger/api/v1"
	"github.com/digital-asset/dazl/go/pkg/encoding"
	"google.golang.org/grpc"
	"time"
)

type V1GRPCLedgerProtocol struct {
	conn     *grpc.ClientConn
	ledgerId string
}

func MakeV1GRPCLedgerProtocol(address string) (*V1GRPCLedgerProtocol, error) {
	var opts []grpc.DialOption
	protocol := V1GRPCLedgerProtocol{}
	opts = append(opts, grpc.WithInsecure())

	conn, err := grpc.Dial(address, opts...)
	if err != nil {
		fmt.Printf("Could not connect to %s\n", address)
		return nil, err
	}

	protocol.conn = conn

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	client := v1.NewLedgerIdentityServiceClient(conn)
	identity, err := client.GetLedgerIdentity(ctx, &v1.GetLedgerIdentityRequest{})
	if err != nil {
		print("Could not fetch ledger identity")
		return nil, err
	}

	protocol.ledgerId = identity.LedgerId
	return &protocol, nil
}

//func (protocol *V1GRPCLedgerProtocol) Submit(commands Commands) error {
//	ctx, cancel := context.WithTimeout(context.Background(), 10 * time.Second)
//	defer cancel()
//
//	request := v1.GetTransactionsRequest{}
//
//	client := v1.NewTransactionServiceClient(protocol.conn)
//	stream, err := client.GetTransactions(ctx, &request)
//	for {
//		tx, err != nul
//		if err == io.EOF {
//			break
//		}
//		log.Println()
//	}
//}
//

// Submit a set of commands to the ledger.
func (protocol *V1GRPCLedgerProtocol) Submit(Commands) error {
	return errors.New("grpc.Submit() not implemented")
}

// Submit a single create command to the ledger, and return the CreatedEvent.
func (protocol *V1GRPCLedgerProtocol) SubmitCreate(CreateCommand) (*CreatedEvent, error) {
	return nil, errors.New("grpc.SubmitCreate() not implemented")
}

// Submit a single create-and-exercise command to the ledger, and return the ExercisedEvent
// that correlates to
func (protocol *V1GRPCLedgerProtocol) SubmitCreateAndExercise(CreateAndExerciseCommand) (*ExercisedEvent, error) {
	return nil, errors.New("grpc.SubmitCreateAndExercise() not implemented")
}

func (protocol *V1GRPCLedgerProtocol) SubmitExercise(ExerciseCommand) (*ExercisedEvent, error) {
	return nil, errors.New("grpc.SubmitExercise() not implemented")
}

func (protocol *V1GRPCLedgerProtocol) SubmitExerciseByKey(ExerciseByKeyCommand) (*ExercisedEvent, error) {
	return nil, errors.New("grpc.SubmitExerciseByKey() not implemented")
}

func (protocol *V1GRPCLedgerProtocol) Query(q QueryRequest) (*EventStream, error) {
	return nil, errors.New("grpc.Query() not implemented")
}

func (protocol *V1GRPCLedgerProtocol) FetchACS(templateIds []string) (*ACS, error) {
	request := v1.GetActiveContractsRequest{
		LedgerId: protocol.ledgerId,
		Filter:   nil,
		Verbose:  true,
	}

	client := v1.NewActiveContractsServiceClient(protocol.conn)
	response, err := client.GetActiveContracts(ctx, &request)
	if err != nil {
		return nil, err
	}

	r, err := response.Recv()
	if err != nil {
		return nil, err
	}

	acs := ACS{}
	for _, contract := range r.ActiveContracts {
		acs.Contracts = append(acs.Contracts, ToEvent(contract))
	}

	return nil, errors.New("grpc.FetchACS() not implemented")
}

func ToEvent(contract *v1.CreatedEvent) *Contract {
	return &Contract{
		TemplateId: ToString(contract.TemplateId),
		ContractId: contract.ContractId,
		Payload:    encoding.RecordToNative(contract.CreateArguments),
	}
}

func ToString(i *v1.Identifier) string {
	return fmt.Sprintf("%s:%s:%s", i.PackageId, i.ModuleName, i.EntityName)
}

func (protocol *V1GRPCLedgerProtocol) FetchPackageIds() ([]string, error) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	request := v1.ListPackagesRequest{
		LedgerId: protocol.ledgerId,
	}

	client := v1.NewPackageServiceClient(protocol.conn)
	response, err := client.ListPackages(ctx, &request)
	if err != nil {
		return nil, err
	}

	return response.PackageIds, nil
}

func (protocol *V1GRPCLedgerProtocol) FetchPackage(packageId string) ([]byte, error) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	request := v1.GetPackageRequest{
		LedgerId:  protocol.ledgerId,
		PackageId: packageId,
	}

	client := v1.NewPackageServiceClient(protocol.conn)
	response, err := client.GetPackage(ctx, &request)
	if err != nil {
		return nil, err
	}

	return response.ArchivePayload, nil
}

func (protocol *V1GRPCLedgerProtocol) UploadPackage(p []byte) error {
	return errors.New("grpc.UploadPackage() not implemented")
}
