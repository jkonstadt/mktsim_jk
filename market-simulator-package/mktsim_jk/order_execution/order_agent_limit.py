"""
Limit Order Agent Module
"""
import logging
from pathlib import PurePath
from .order_agent import OrderAgent
from ..order_management.order_book import OrderBook

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, encoding='utf-8', level=logging.INFO)
log = logging.getLogger(PurePath(__file__).name)


class LimitOrderAgent(OrderAgent):
    """
    Limit order agent - execution when price tick events occur
    """

    def __init__(self) -> None:
        """
        Agent contains the order book details.

        :param self: Represent the instance of the class
        :return: New Object
        """
        self.order_book = OrderBook()

    def add_order(self, side: bool, symbol: str, quantity: int, limit: float):
        """
        The add_order function is used to add an order to the order_book.
        The function takes in a side, symbol, quantity and limit as parameters.
        It then creates an Order object using these parameters and adds it to the
        order_book.

        :param self: Represent the instance of the class
        :param side: bool: Determine whether the order is a buy or sell
        :param symbol: str: Identify the symbol of the order
        :param quantity: int: Specify the number of shares to be traded
        :param limit: float: Set the limit price for the order
        :return: An order object
        """
        order = self.order_book.add_order(side, symbol, quantity, limit)
        log.debug("Added to order to order_execution agent: %s", order.format_order())

    def price_check(self, symbol: str, bid_price: float, ask_price: float):
        """
        Modeled from abstract class, implementing the limit order specific check.

        :param symbol: symbol
        :param bid_price: current market bid
        :param ask_price: current market ask
        """
        log.debug("Checking market data: %s, %5.2f | %5.2f", symbol, bid_price, ask_price)
        self.order_book.check_tick(symbol, bid_price, ask_price)

    def print_book(self, verbiage):
        """
        The print_book function prints the order book.

        :param self: Represent the instance of the class
        :param verbiage: Print the order book with specific text
        :return: The order_book
        """
        self.order_book.print_all(verbiage)
