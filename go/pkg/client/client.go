package client

import (
	"github.com/digital-asset/dazl-client/go/pkg/protocol"
	"net/url"
)

type Client struct {
	Url string
	//Packages *PackageService
	Protocol protocol.LedgerProtocol
}

func (client *Client) Connect(address string) error {
	grpcProtocol, err := protocol.MakeV1GRPCLedgerProtocol(address)
	if err == nil {
		client.Protocol = grpcProtocol
		return nil
	}
	print(err)

	addrUrl, err := url.Parse(address)

	httpProtocol, err := protocol.MakeV1HTTPLedgerProtocol(addrUrl)
	if err == nil {
		client.Protocol = httpProtocol
		return nil
	}

	return err
}

func (client *Client) Submit(commands protocol.Commands) error {
	return client.Protocol.Submit(commands)
}
