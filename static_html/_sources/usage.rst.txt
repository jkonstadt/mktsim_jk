Usage
=====

.. _execution:

Virtual Environment
-------------------

To source the virtual environment

.. code-block:: console

    $ source .venv/bin/activate

*To confirm*

If you have sourced it correctly, you will now see .venv as part of the prompt

.. code-block:: console

    (.venv) $

Market Publisher
----------------

To run the market publisher on its own and print the change in
price to the screen, you can run execute market_publisher.py

.. code-block:: console

   (.venv) $ cd market-simulator-package/mktsim_jk/publishers
   (.venv) $ ./market_publisher.py

*example*

.. code-block:: console

    (.venv) $ python market_publisher.py
    2023-05-05 01:14:13,288 [DEBUG] asyncio - Using selector: KqueueSelector
    TIME       TICKER       BID |     ASK
    --------   -------- ------- | -------
    2023-05-05 01:14:13,289 [INFO] market_publisher.py - Seconds until market closes: 5
    01:14:14 - IBM       102.00 |  103.00
    01:14:15 - IBM       101.75 |  102.00

Executing Tests
---------------

To execute, run the test script in the parent directory of the mktsim_jk package

.. code-block:: console

    (.venv) $ cd market-sumulator
    (.venv) $ python limit_order_agent_tests.py

    2023-05-05 01:18:47,259 [INFO] limit_order_agent_tests.py - Testing BUY at order_execution
    2023-05-05 01:18:47,259 [DEBUG] order.py - Order created: [BUY 1,000 IBM @ 100.00] OPEN
    2023-05-05 01:18:47,259 [DEBUG] limit_order_agent.py - Added to order to order_execution agent: [BUY 1,000 IBM @ 100.00] OPEN
    2023-05-05 01:18:47,259 [DEBUG] asyncio - Using selector: KqueueSelector

