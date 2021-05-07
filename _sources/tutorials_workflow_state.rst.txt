.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
.. _tutorials_workflow_state:

Workflow State Example
======================

The purpose of this example is to demonstrate a multi-contract-creation dependency use-case: a sitution where the application must wait for multiple contracts to be created before it can proceed to the next step. This is similar to the "Message Ingester" sample application, but with the key difference that the state transitions in the "Message Ingester" workflow each depend solely on a single contract creation.

The workflow involving three parties: ``Alice``, ``Bob``, and ``Operator``. When writing a DAML
application, we recommend the following steps:

   1. Describe your workflow as a series of contracts in DAML.
   2. Write one or more DAML test scenarios that walk through each step of the workflow, starting from creation of the genesis contract, through a sequence of ``exercise`` commands, to the final state of the workflow. (Note: The DAML test scenarios are used for verifying the steps of the workflow in a sequential manner. However, when the workflow is deployed to a live platflorm, the events that prompt steps in the workflow to move forward cannot be assumed to occur sequentially.)
   3. Write your application.
   4. Test your application on the sandbox. The ledger server implements the same API, so performance testing can be done with the same application.


The workflow for this application is as follows:

1. The ``GenesisContract``, is created. It describes the operation(s) that the operator of this workflow can perform. In this example, we have assigned the party name ``Operator`` to the GenesisContract.
2. ``Operator`` invites the ``Bob`` to be the ticket seller, and also invites ``Alice`` to be the ticket buyer.
3. Only after BOTH ``Alice`` and ``Bob`` have accepted their respective invitations  can the workflow progress to the next state (``TicketTransactionsInProgress``)
4. A ticket transaction occurs.
5. The workflow is completed.

DAML Model
----------

``WorkflowStateExample.daml``

.. literalinclude:: ../tests/tutorials/workflow_state/daml/WorkflowStateExample.daml
    :language: daml

The ``ticketTransactionTest`` scenario describes a sample execution of the workflow, and is the basis from from which
our Python application will be designed.

Python Application
------------------

``store.py``

.. literalinclude:: ../tests/tutorials/workflow_state/store.py
    :language: python

``workflow_state_example.py``

.. literalinclude:: ../tests/tutorials/workflow_state/workflow_state_example.py
    :language: python

To run this code sample:
   1. Download the SDK
   2. create a new project: ``da new my-project-name-here``
   3. ``cd my-project-name-here``
   4. Create a file, WorkflowStateExample.daml, that contains the above listed DAML.
   5. Create a file, workflow_state_sample.py, that contains the Python code for "workflow_state_example.py" listed above.
   6. Create a file, store.py, that contains, that contains the Python code for "store.py" listed above.
   7. Download the dazl-starter template (which also creates a Python venv): ``da project add dazl-starter``
   8. Run the application: ``./venv/bin/python3 workflow_state_example.py``

:func:`accept_ticket_seller_invite` and :func:`accept_ticket_buyer_invite` store their respective contracts into ``contract_store``. This is the first step in setting up a multi-contract-creation dependency.

.. literalinclude:: ../tests/tutorials/workflow_state/workflow_state_example.py
    :language: python
    :start-after: # DOC_BEGIN: FUNCTION_ACCEPT_INVITE
    :end-before: # DOC_END: FUNCTION_ACCEPT_INVITE

:func:`transition_to_ticket_transactions_in_progress` performs lookups into ``contract_store``. These lookups will wait until the specified contract keys are present in the ``contract_store``, and only perform the ``exercise`` command after that point. Thus, BOTH the `TicketSellerRole` and the `TicketBuyerRole` must be created before the application can transition to the next step in the workflow.

.. literalinclude:: ../tests/tutorials/workflow_state/workflow_state_example.py
    :language: python
    :start-after: # DOC_BEGIN: FUNCTION_MULTI_CREATION_DEPENDENCY
    :end-before: # DOC_END: FUNCTION_MULTI_CREATION_DEPENDENCY

Application Output
------------------

This application will produce this output::

  [Info] Starting:
      Sandbox ledger server
      .../daml/WorkflowStateExample.daml
      with no scenario and binding to port 7600
  Waiting for Sandbox...ok
  5 total contracts over 5 templates
  +-- party 'Alice' (block heights 2 to 9)
  |+- party 'Bob' (block heights 2 to 9)
  ||+ party 'Operator' (block heights 1 to 9)
  |||

  WorkflowStateExample.GenesisContract (1 contract) ----------------------------------------------------------------------
      #cid operator
    C 0:0_ Operator

  WorkflowStateExample.TicketBuyerRole (1 contract) ----------------------------------------------------------------------
      #cid operator ticketBuyer
  C   2:2_ Operator Alice

  WorkflowStateExample.TicketPurchaseAgreement (1 contract) --------------------------------------------------------------
      #cid operator ticketBuyer ticketSeller
  CC  6:2_ Operator Alice       Bob

  WorkflowStateExample.TicketSellerRole (1 contract) ---------------------------------------------------------------------
      #cid operator ticketSeller
   C  3:2_ Operator Bob

  WorkflowStateExample.WorkflowCompleted (1 contract) --------------------------------------------------------------------
      #cid operator
    C 7:2_ Operator
  stopping... Sandbox ledger server
  .../daml/WorkflowStateExample.daml
  with no scenario and binding to port 7600

  Process finished with exit code 0

Thus, a ``TicketPurchaseAgreement`` is created. Also note that the contracts representing intermediate steps in the workflow (``WorkflowSetupInProgress``, and ``WorkflowTicketTransactionsInProgress``) were created and then subsequently archived. Only the contract representing the final state, ``WorkflowCompleted`` is active.
