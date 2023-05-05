Testing
=======

Test Routines
-------------

These simple tests create an order book with a single order,
start the market with a direction that will likely result in a
marketable price, and then confirm the order was executed.

There are 3 tests

* the first test simply starts the publisher
* the second test creates a buy order and confirms it executs if the price is marketable
* the third test creates a sell order and confirms it executes if the price is marketable

To execute, run the test script in the parent directory of the mktsim_jk package

.. code-block:: console

    (.venv) $ cd market-simulator-package
    (.venv) $ python order_agent_limit_tests.py
    2023-05-05 01:18:47,259 [INFO] order_agent_limit_tests.py - Testing BUY at order_execution
    2023-05-05 01:18:47,259 [DEBUG] order.py - Order created: [BUY 1,000 IBM @ 100.00] OPEN
    2023-05-05 01:18:47,259 [DEBUG] limit_order_agent.py - Added to order to order_execution agent: [BUY 1,000 IBM @ 100.00] OPEN
    2023-05-05 01:18:47,259 [DEBUG] asyncio - Using selector: KqueueSelector

*Successful Execution*

.. code-block:: console

    ----------------------------------------------------------------------
    Ran 3 tests in 10.009s

    OK

Test Code
---------

.. function:: OrderAgentLimitTest.test_order_book()

        Adds an order to the book and confirms that it is reflected in the book

        The test_order_book function tests the OrderBook class.
        It creates an order book object, adds a buy order to it, and then prints out the contents of the order book.
        The test_order_book function also checks that there is one buy order in the book.

        :return: Test result

.. function:: OrderAgentLimitTest.test_sell_success()

        Tests a sell order in a rising market.

        * initialize market to be increasing
        * add a limit order above current bid

        The function creates a MarketPublisher object and sets its callback to be the on_price_tick method of
        the LimitOrderAgent object. The market publisher is configured to start at 98 and move above low of 100,
        and then it publishes prices for IBM stock. The test passes if there is one completed order in the order book.

        :return: Test result

.. function:: OrderAgentLimitTest.test_buy_success()

        Tests a buy order in a falling market.

        * initialize market to be decreasing
        * add a limit order below current ask

        The test_buy_success function tests the LimitOrderAgent's ability to buy a stock.
        The function creates a MarketPublisher object, which is used to simulate market data.
        The function then creates a LimitOrderAgent object and adds an order for 1000 shares of IBM at 100 dollars per share.
        Finally, the test runs the MarketPublisher and checks that there is one completed order in the book.

        :return: Test result








