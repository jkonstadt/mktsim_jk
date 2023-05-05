""" Test scripts for order agent of order type = limit """
import asyncio
import logging
import unittest
from pathlib import PurePath
from mktsim_jk.order_management.order_book import OrderBook
from mktsim_jk.publishers.market_publisher import MarketPublisher
from mktsim_jk.order_execution.order_agent_limit import LimitOrderAgent


LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, encoding='utf-8', level=logging.DEBUG)
log = logging.getLogger(PurePath(__file__).name)


class LimitOrderAgentTest(unittest.TestCase):
    """Test Execution facility"""

    def test_order_book(self):
        """
        Adds an order to the book and confirms that it is reflected in the book

        The test_order_book function tests the OrderBook class.
        It creates an order book object, adds a buy order to it, and then prints out the
        contents of the order book. The test_order_book function also checks that there
        is one buy order in the book.

        :return: Test result
        """
        log.info("*** Order book test ***")
        order_book = OrderBook()
        order_book.add_order(False, "IBM", 1000, 105.0)
        order_book.print_all("TESTING ORDER_BOOK ORDER CREATION")
        self.assertTrue(order_book.get_qty_orders() == 1)

    def test_sell_success(self):
        """
        Tests a sell order in a rising market.

        * initialize market to be increasing
        * add a limit order above current bid

        The function creates a MarketPublisher object and sets its callback to be the on_price_tick method of
        the LimitOrderAgent object. The market publisher is configured to start at 98 and move above low of 100,
        and then it publishes prices for IBM stock. The test passes if there is one completed order in the order book.

        :return: Test result
        """
        log.info("Testing sell at order_execution")

        market_open = {"IBM": 98}
        market_direction = 1
        market = MarketPublisher(market_open=market_open, market_direction=market_direction, output=True)

        loa = LimitOrderAgent()
        market.set_callback(loa.price_check)
        # SELL 1000 IBM @ 100
        loa.add_order(False, "IBM", 1000, 100.00)
        asyncio.run(market.start_publishing())
        loa.print_book("SELL ORDER TEST")
        self.assertTrue(loa.order_book.get_completed_qty_orders() == 1)

    def test_buy_success(self):
        """
        Tests a buy order in a falling market.

        * initialize market to be decreasing
        * add a limit order below current ask

        The test_buy_success function tests the LimitOrderAgent's ability to buy a stock.
        The function creates a MarketPublisher object, which is used to simulate market data.
        The function then creates a LimitOrderAgent object and adds an order for 1000 shares
        of IBM at 100 dollars per share. Finally, the test runs the MarketPublisher and checks
        that there is one completed order in the book.

        :return: Test result
        """
        log.info("Testing BUY at order_execution")

        # Configures market to start at 102 and move down to high of 100
        market_open = {"IBM": 102}
        market_direction = -1
        mi = MarketPublisher(market_open=market_open, market_direction=market_direction
                             , output=True)
        loa = LimitOrderAgent()
        mi.set_callback(loa.price_check)
        # BUY 1000 IBM @ 100
        loa.add_order(True, "IBM", 1000, 100.00)
        asyncio.run(mi.start_publishing())
        loa.print_book("BUY ORDER TEST")
        self.assertTrue(loa.order_book.get_completed_qty_orders() == 1)


if __name__ == '__main__':
    unittest.main()
