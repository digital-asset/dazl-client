package protocol

// LedgerOProtocol interface defines protocol/transport-specific implementations of common ledger
// operations. These loosely correlate to the current set of gRPC Ledger API and HTTP-JSON API
// services.
type LedgerProtocol interface {

	// Submit a set of commands to the ledger.
	Submit(Commands) error

	// Submit a single create command to the ledger, and return the CreatedEvent.
	SubmitCreate(CreateCommand) (*CreatedEvent, error)

	// Submit a single create-and-exercise command to the ledger, and return the ExercisedEvent
	// that correlates to
	SubmitCreateAndExercise(CreateAndExerciseCommand) (*ExercisedEvent, error)
	SubmitExercise(ExerciseCommand) (*ExercisedEvent, error)
	SubmitExerciseByKey(ExerciseByKeyCommand) (*ExercisedEvent, error)
	Query(q QueryRequest) (*EventStream, error)
	FetchACS(templateIds []string) (*ACS, error)
	FetchPackageIds() ([]string, error)
	FetchPackage(string) ([]byte, error)
	UploadPackage(p []byte) error
}
