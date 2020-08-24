.. Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
.. _tutorials_message_ingester:

Message Ingester
================

This example sets up a workflow involving two parties, ``Alice`` and ``Bob``. When writing a DAML
application, we recommend the following steps:

   1. Describe your workflow as a series of contracts in DAML.
   2. Write one or more DAML test scenarios that walk through each step of the workflow, starting from creation of the genesis contract, through a sequence of ``exercise`` commands, to the final state of the workflow. (Note: The DAML test scenarios are used for verifying the steps of the workflow in a sequential manner. However, when the workflow is deployed to a live platflorm, the events that prompt steps in the workflow to move forward cannot be assumed to occur sequentially.)
   3. Write your application.
   4. Test your application on the sandbox. The ledger server implements the same API, so performance testing can be done with the same application. 

The Message Ingester workflow is as follows:

1. The genesis contract, ``OperatorRole``, is created. The ``OperatorRole`` contract is a contract that describes the operation(s) that the operator of this workflow can perform. In this example, we have assigned the party name ``Alice`` to the OperatorRole.
2. ``Alice`` ingests an input message, which causes the generation of a ``TradeRequest`` contract.
3. ``Bob`` is the ``requestProcessingParty`` on the ``TradeRequest`` contract, and exercises the
   ``AcceptMessage`` choice on the ``TradeRequest``. This causes the generation of a ``TradeResponse`` contract.
4. ``Alice`` exercises the ``Acknowledge`` choice on the ``TradeResponse`` contract.
   This causes the generation of a ``WorkflowCompleted`` contract.

DAML Model
----------

This example assumes the following DAML:

.. literalinclude:: ../tests/tutorials/message_ingester/MessageIngester.daml
    :language: daml

The ``messageIngesterTest`` scenario describes a sample execution of the workflow, and is the basis from from which
our Python application will be designed.

Python Application
------------------

.. literalinclude:: ../tests/tutorials/message_ingester/message_ingester.py
    :language: python
    :linenos:

To run this code sample:
   1. Download the SDK
   2. create a new project: ``da new my-project-name-here``
   3. ``cd my-project-name-here``
   4. Create a file, MessageIngester.daml, that contains the above listed DAML.
   5. Createa  file, message_ingester.py, that contains the above listed Python code.
   6. Download the dazl-starter template (which also creates a Python venv): ``da project add dazl-starter``
   7. Start the sandbox: ``da sandbox``
   8. Run the application: ``./venv/bin/python3 message_ingester.py``

:func:`run` configures client_mgr such that it will invoke the :func:`work` function after
it has successfully connected to the platform/sandbox.

:func:`work` contains a command to create the genesis contract, and a series of callback registrations,
each of which provide a reference to a custom python function that shall be invoked when a certain
leger event occurs. For example, this registration:

.. literalinclude:: ../tests/tutorials/message_ingester/message_ingester.py
    :language: python
    :start-after: # DOC_BEGIN: SAMPLE_CALLBACK_ONCREATED
    :end-before: # DOC_END: SAMPLE_CALLBACK_ONCREATED

indicates that the :func:`ingest_the_message` shall be invoked after the ``OperatorRole`` contract is
created.

:func:`ingest_the_message` describes what will happen when at ``on_created`` event occurs:
  1. The DAZL framework, upon detecting the specified ``on_created`` event, will invoke this function and pass it the contract id (``cid``) and corresponding contract parameters (``cdata``).
  2. An ``exercise`` choice will be performed on the contract (in this case, it's an ``OperatorRole`` contract)
  3. That ``exercise`` choice will be invoked on a DAML contract with a contract id of ``cid``, with the specified parameters.
  4. Since this is a non-consuming choice, the ``OperatorRole`` contract will remain active.

.. literalinclude:: ../tests/tutorials/message_ingester/message_ingester.py
    :language: python
    :start-after: # DOC_BEGIN: FUNCTION_INGEST_THE_MESSAGE
    :end-before: # DOC_BEGIN: FUNCTION_INGEST_THE_MESSAGE

The :func:`exercise` call in the above code snippet corresponds to this line in our DAML test scenario:

.. literalinclude:: ../tests/tutorials/message_ingester/MessageIngester.daml
    :language: daml
    :start-after: -- DOC_BEGIN: SAMPLE_DAML_SCENARIO_INGEST_MESSAGE
    :end-before: -- DOC_END: SAMPLE_DAML_SCENARIO_INGEST_MESSAGE

Thus, a typical application would have a similar structure to :func:`work` in that it will contain only one command
to create the genesis contract, and all other code will describe the callback handlers and the situations under which
those callbacks shall be invoked.

Application Output
------------------

This application will produce this output::

  2 total contracts over 2 templates
  +- party 'Alice' (block heights 1 to 5)
  |+ party 'Bob' (block heights 2 to 5)
  ||

  MessageIngester.OperatorRole (1 contract) ------------------------------------------------------------------------------
  #cid operator
  C  0:0_ Alice

  MessageIngester.WorkflowCompleted (1 contract) -------------------------------------------------------------------------
  #cid acknowledgingParty originalMessageIngestedTime TradeResponseAcknowledgedTime
  C  3:2_ Alice              1970-01-01T00:00:00Z        1970-01-01T00:00:00Z

The ``TradeRequest`` and ``TradeResponse`` contracts were created, and subsequently archived during the course
of the workflow, thus only ``OperatorRole`` ``WorkflowCompleted`` and (which has no consuming choices) are active on the ledger
when this application terminates.
