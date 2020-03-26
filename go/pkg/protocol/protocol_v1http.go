package protocol

import (
	"bytes"
	"encoding/json"
	"errors"
	"log"
	"net/http"
	"net/url"
)

var createURL *url.URL
var exerciseURL *url.URL

func init() {
	var err error
	createURL, err = url.Parse("v1/create")
	if err != nil {
		log.Fatal("Error creating URL constants")
	}

	exerciseURL, err = url.Parse("v1/exercise")
	if err != nil {
		log.Fatal("Error creating URL constants")
	}
}

type V1HTTPLedgerProtocol struct {
	Client  *http.Client
	BaseURL url.URL
}

type QueryRequest struct {
	TemplateIds []string
}

type EventStream interface {
	Read() (*Event, error)
	Close() error
}

func MakeV1HTTPLedgerProtocol(baseURL *url.URL) (V1HTTPLedgerProtocol, error) {
	return V1HTTPLedgerProtocol{Client: new(http.Client), BaseURL: *baseURL}, nil
}

func (p V1HTTPLedgerProtocol) FetchACS(templateIds []string) (*ACS, error) {
	return nil, errors.New("not implemented")
}

func (p V1HTTPLedgerProtocol) Query(q QueryRequest) (*EventStream, error) {
	return nil, errors.New("not implemented")
}

type ACS struct {
	Contracts []Contract
}

type Contract struct {
	TemplateId string
	ContractId string
	Payload    map[string]interface{}
}

func (p V1HTTPLedgerProtocol) Submit(command Commands) error {
	for _, cmd := range command.Commands {
		switch c := cmd.(type) {
		case CreateCommand:
			_, err := p.SubmitCreate(c)
			if err != nil {
				return err
			}
		case CreateAndExerciseCommand:
			_, err := p.SubmitCreateAndExercise(c)
			if err != nil {
				return err
			}
		case ExerciseCommand:
			_, err := p.SubmitExercise(c)
			if err != nil {
				return err
			}
		case ExerciseByKeyCommand:
			_, err := p.SubmitExerciseByKey(c)
			if err != nil {
				return err
			}
		}
	}

	return nil
}

func (p V1HTTPLedgerProtocol) SubmitCreate(command CreateCommand) (*CreatedEvent, error) {
	return submitCreate(&p, command)
}

func (p V1HTTPLedgerProtocol) SubmitCreateAndExercise(command CreateAndExerciseCommand) (*ExercisedEvent, error) {
	return submitExercise(&p, command)
}

func (p V1HTTPLedgerProtocol) SubmitExercise(command ExerciseCommand) (*ExercisedEvent, error) {
	return submitExercise(&p, command)
}

func (p V1HTTPLedgerProtocol) SubmitExerciseByKey(command ExerciseByKeyCommand) (*ExercisedEvent, error) {
	return submitExercise(&p, command)
}

func (p V1HTTPLedgerProtocol) FetchPackageIds() ([]string, error) {
	return nil, errors.New("not implemented")
}

func (p V1HTTPLedgerProtocol) FetchPackage(packageId string) ([]byte, error) {
	return nil, errors.New("not implemented")
}

func (p V1HTTPLedgerProtocol) UploadPackage(darPackage []byte) error {
	return errors.New("not implemented")
}

func submit(p *V1HTTPLedgerProtocol, u *url.URL, command Command, v interface{}) error {
	body, err := json.Marshal(command)
	if err != nil {
		return err
	}

	fullURL := p.BaseURL.ResolveReference(u).String()
	response, err := p.Client.Post(fullURL, "application/json", bytes.NewBuffer(body))
	if err != nil {
		return err
	}

	return json.NewDecoder(response.Body).Decode(v)
}

func submitCreate(p *V1HTTPLedgerProtocol, command Command) (*CreatedEvent, error) {
	var evt CreatedEvent
	err := submit(p, createURL, command, &evt)
	if err != nil {
		return nil, err
	}
	return &evt, nil
}

func submitExercise(p *V1HTTPLedgerProtocol, command Command) (*ExercisedEvent, error) {
	var evt ExercisedEvent
	err := submit(p, exerciseURL, command, &evt)
	if err != nil {
		return nil, err
	}
	return &evt, nil
}
