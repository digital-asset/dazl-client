_NS_LEDGER_ID_DEPRECATED = (
    "fetching ledger_id from an event is deprecated; instead get it from the connection (or "
    "consider if knowing the ledger ID is important to your usecase)"
)

_NS_ACS_DEPRECATED = (
    "acs functions are deprecated; you should keep your own store, or use contract keys to avoid "
    "needing to work with local state"
)


COMMAND_ID = "command_id is no longer accessible in the new API"
WORKFLOW_ID = "workflow_id is no longer accessible in the new API"
EVENT_ID = "event_id is no longer accessible in the new API"
WITNESS_PARTIES = "witness_parties is no longer accessible in the new API"
PARTY = "reading `party` from a connection is ambiguous when multi-party submissions are being used; consider an alternate way of determining an appropriate Party in this context"
