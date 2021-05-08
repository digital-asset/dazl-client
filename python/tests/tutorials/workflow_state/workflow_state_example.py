# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import subprocess

from dazl import create, exercise
from dazl.client import create_client
from dazl.plugins import LedgerCapturePlugin
from store import ContractStore

operator = "Operator"
alice = "Alice"
bob = "Bob"

parties = [operator, alice, bob]
url = "http://localhost:7600/"
contract_store = ContractStore()
transaction_limit = 1


def create_initial_workflow_state(cid, cdata):
    workflow_state = [exercise(cid, "SetInitialWorkflowState", {})]
    return workflow_state


def invite_ticket_seller(cid, cdata):
    """Workflow state: WorkflowSetupInProgress"""
    ticket_seller_invitation = [exercise(cid, "InviteTicketSeller", {"ticketSeller": bob})]
    return ticket_seller_invitation


def invite_ticket_buyer(cid, cdata):
    """Workflow state: WorkflowSetupInProgress"""
    ticket_buyer_invitation = [exercise(cid, "InviteTicketBuyer", {"ticketBuyer": alice})]
    return ticket_buyer_invitation


# DOC_BEGIN: FUNCTION_ACCEPT_INVITE
def accept_ticket_seller_invite(cid, cdata):
    """Workflow state: WorkflowSetupInProgress"""
    ticket_seller_role = [exercise(cid, "AcceptTicketSellerInvitation", {})]
    contract_store.save("ticketSellerRole1", cid, cdata)
    return ticket_seller_role


def accept_ticket_buyer_invite(cid, cdata):
    """Workflow state: WorkflowSetupInProgress"""
    ticket_buyer_role = [exercise(cid, "AcceptTicketBuyerInvitation", {})]
    contract_store.save("ticketBuyerRole1", cid, cdata)
    return ticket_buyer_role


# DOC_END: FUNCTION_ACCEPT_INVITE

# DOC_BEGIN: FUNCTION_MULTI_CREATION_DEPENDENCY
async def transition_to_ticket_transactions_in_progress(cid, cdata):
    await contract_store.find("ticketSellerRole1")
    await contract_store.find("ticketBuyerRole1")
    workflow_ticket_transactions_in_progress = [exercise(cid, "TicketTransactionsInProgress", {})]
    contract_store.save("workflowTicketTransactionsInProgress", cid, cdata)
    return workflow_ticket_transactions_in_progress


# DOC_END: FUNCTION_MULTI_CREATION_DEPENDENCY


async def offer_ticket_purchase_agreement(cid, cdata):
    """Workflow state: WorkflowTicketTransactionsInProgress"""
    await contract_store.find("workflowTicketTransactionsInProgress")
    offer_ticket_purchase_agreement = [
        exercise(cid, "OfferTicketPurchaseAgreement", {"ticketBuyer": alice})
    ]
    global transaction_limit
    if transaction_limit > 0:
        transaction_limit -= 1
        return offer_ticket_purchase_agreement


def purchase_ticket(cid, cdata):
    """Workflow state: WorkflowTicketTransactionsInProgress"""
    ticket_purchase_agreement = [exercise(cid, "PurchaseTicket", {})]
    return ticket_purchase_agreement


def save_purchase_agreement(cid, cdata):
    """Workflow state: WorkflowTicketTransactionsInProgress"""
    contract_store.save("purchase_agreement", cid, cdata)


async def transition_to_workflow_completed(cid, cdata):
    await contract_store.find("purchase_agreement")
    # move on to the next phase of the workflow after 1 purchase agreement has been created
    workflow_completed = [exercise(cid, "WorkflowCompleted", {})]
    return workflow_completed


def register_event_handlers(client_mgr):
    """
    Register event handlers with the appropriate clients.
    """

    # initial workflow state (1 of 3): "InviteParticipantsInProgress"

    # Define a ledger client associated with the 'Operator' party, and how it reacts to events
    operator_client = client_mgr.new_client("Operator")
    operator_client.on_created(
        "WorkflowStateExample.GenesisContract", create_initial_workflow_state
    )
    operator_client.on_created("WorkflowStateExample.GenesisContract", invite_ticket_seller)
    operator_client.on_created("WorkflowStateExample.GenesisContract", invite_ticket_buyer)

    # define a ledger client associated with the ticket seller, and how it reacts to events
    bob_client = client_mgr.new_client(bob)
    bob_client.on_created(
        "WorkflowStateExample.TicketSellerInvitation", accept_ticket_seller_invite
    )

    # define a ledger client associated with the ticket buyer, and how it reacts to events
    alice_client = client_mgr.new_client(alice)
    alice_client.on_created(
        "WorkflowStateExample.TicketBuyerInvitation", accept_ticket_buyer_invite
    )

    # transition to workflow state: "TicketTransactionsInProgress"
    operator_client.on_created(
        "WorkflowStateExample.WorkflowSetupInProgress",
        transition_to_ticket_transactions_in_progress,
    )

    # workflow state (2 of 3): "TicketTransactionsInProgress"
    bob_client.on_created("WorkflowStateExample.TicketSellerRole", offer_ticket_purchase_agreement)

    # alice purchases a ticket
    alice_client.on_created("WorkflowStateExample.TicketPurchaseAgreementOffer", purchase_ticket)
    alice_client.on_created("WorkflowStateExample.TicketPurchaseAgreement", save_purchase_agreement)

    # transition to workflow state (3 of 3): "WorkflowCompleted"
    operator_client.on_created(
        "WorkflowStateExample.WorkflowTicketTransactionsInProgress",
        transition_to_workflow_completed,
    )

    # all event handlers are defined; create the genesis contract, and all other event handlers shall react thereafter
    operator_client.submit(
        [create("WorkflowStateExample.GenesisContract", {"operator": "Operator"})]
    )


def run():

    with create_client(parties=parties, participant_url=url) as client_mgr:
        inspector = LedgerCapturePlugin.stdout()
        try:
            client_mgr.register(inspector)
            register_event_handlers(client_mgr)
            ledger_run = client_mgr.run_until_complete()
            return ledger_run.exit_code
        finally:
            inspector.dump_all()
            subprocess.Popen(["da", "stop"]).wait()


if __name__ == "__main__":
    subprocess.Popen(["da", "sandbox"]).wait()
    run()
