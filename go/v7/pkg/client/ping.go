package client

import (
	"context"
	"log"

	"google.golang.org/grpc"

	v1 "github.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1"
)

type LedgerId string

// GetLedgerId attempts to connect to a ledger at the specified host:port and fetch the ledger ID.
func GetLedgerId(ctx context.Context, target string) (LedgerId, error) {
	conn, err := grpc.DialContext(ctx, target, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return "", err
	}

	client := v1.NewLedgerIdentityServiceClient(conn)
	response, err := client.GetLedgerIdentity(ctx, &v1.GetLedgerIdentityRequest{})
	if err != nil {
		return "", err
	}

	log.Printf("Successful ping; the ledger ID is %s", response.LedgerId)
	return LedgerId(response.LedgerId), nil
}
