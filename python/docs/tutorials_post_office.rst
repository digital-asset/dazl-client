.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
.. _tutorials_post_office:

Post Office
===========

This example sets up a post office, with a ``Postman`` who routes letters, instances of ``Author``
who send letters, and instances of ``Receiver`` who receive letters.

Each author, when instantiated, will immediately send letters to five of their friends.

DAML Model
----------

This example assumes the following DAML:

.. literalinclude:: ../tests/tutorials/post_office/Main.daml
    :language: daml

Create the Postman
------------------

The Postman serves as the operator of this market, and its role contract must be defined before
anything else can happen:

If you are running this code example through the SDK, it will:
  1. start up a Ledger Sandbox in the background, point it to the above DAML model,
  2. run the code against that Ledger Sandbox, and
  3. stop the Ledger Sandbox.

First, a few important imports:

.. literalinclude:: ../tests/tutorials/post_office/tutorial.py
    :language: python
    :start-after: # DOC_BEGIN: IMPORTS_CONSTANTS
    :end-before: # DOC_END: IMPORTS_CONSTANTS
    :name: imports_and_constants

Then the main dish:

.. literalinclude:: ../tests/tutorials/post_office/tutorial.py
    :language: python
    :dedent: 4
    :start-after: # DOC_BEGIN: CREATE_POSTMAN
    :end-before: # DOC_END: CREATE_POSTMAN
    :name: run_test_create_postman

Lastly, the code that actually runs everything:

.. literalinclude:: ../tests/tutorials/post_office/tutorial.py
    :language: python
    :dedent: 4
    :start-after: # DOC_BEGIN: MAIN-BOILERPLATE
    :end-before: # DOC_END: MAIN-BOILERPLATE


:func:`dazl.simple_client` is a helper function for creating a :class:`Network` and a
:class:`SimplePartyClient`. At a minimum, you must provide it a list of parties to listen as, and a URL to the Sandbox
(or Ledger Server participant node when running against a real instance).

To create a client for a specific party, call :meth:`LedgerClientManager.new_client`. There are
several key methods on it; this example introduces ``ParticipantLedgerClient.on_ready``, which is
called when the connection to the ledger is initialized. The parameters are ignored at this point.
The callback, like most callbacks, can return a ``Command`` to submit to the ledger. In this
example, a ``Main:PostmanRole`` contract is to be created with one argument named ``postman``
and a value of ``'Postman'``

Finally, to actually start the manager and all the clients, call
``LedgerClientManager.run_until_complete``. The code should run and return an exit code of 0,
indicating that the script successfully ran. But what if you wanted to actually see what happened
to the ledger afterwards?


Inspect the Ledger
------------------

Using the convenience ``sandbox()`` method makes development a bit quicker, but it is difficult to
actually see what is happening afterwards because it tears down the ledger and all of its state.
You could either start a Sandbox instance manually through the SDK, or you could output the ledger
after every run:

.. literalinclude:: ../tests/tutorials/post_office/tutorial.py
    :language: python
    :dedent: 4
    :start-after: # DOC_BEGIN: INSPECT_LEDGER
    :end-before: # DOC_END: INSPECT_LEDGER

We have added :class:`dazl.plugin.LedgerCapturePlugin`, which listens for events from the ledger and
stores them internally to be drawn out later. The main body of ``run_test`` outputs the result of
the ledger in a ``try``/``finally`` block so that the ledger is always printed out, even if an
exception occurs.

:class:`dazl.plugin.LedgerCapturePlugin` exposes several class methods for easily creating an
instance; in this example, ``LedgerCapturePlugin`` outputs its results to ``stdout`` when
``dump_all`` is called.


Set up participants
-------------------

We have now created the postman and can see that on the ledger; now we'll add the other participants
of this market. For readability, let's also split out all the registration methods into a separate
``set_up`` function so that we can keep the focus on adding listeners to the ledger:

.. literalinclude:: ../tests/tutorials/post_office/tutorial.py
    :language: python
    :dedent: 4
    :start-after: # DOC_BEGIN: INVITE_PARTICIPANTS
    :end-before: # DOC_END: INVITE_PARTICIPANTS

The ``on_created`` method allows you to add an event handler for templates as they are created on
the ledger. Like the ``on_ready`` method above, you can return a ``Command`` (or in this case, a
``list`` of ``Command``) that is to be executed in response to this event.

After running the script, you should see a few more columns in the output for all the new parties,
and you can see that the parties now see invitation contracts that they can exercise choices on. To
further progress the workflow, let's add more callbacks in ``set_up``:

.. literalinclude:: ../tests/tutorials/post_office/tutorial.py
    :language: python
    :dedent: 4
    :start-after: # DOC_BEGIN: ACCEPT_INVITES
    :end-before: # DOC_END: ACCEPT_INVITES

Now notice that the ``InviteAsAuthor`` and ``InviteAsReceiver`` contracts are no longer in the
output, instead replaced with ``AuthorRole`` and ``ReceiverRole`` contracts; that's because the
``Accept`` choice on these contracts is a consuming choice.

In order to respond to these contracts as other parties, we have also created new clients, one for
every additional party. Now that we have a universe of participants fully set up and ready to go,
let's do some actual work.


Send some "letters" through the post office
-------------------------------------------

Once a participant's ``Main:AuthorRole`` is created, that participant is now granted the ability to
send letters to other participants in the market.

-- TBC --

