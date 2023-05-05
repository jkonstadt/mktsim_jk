""" Order object definition """
from pathlib import PurePath
from datetime import datetime
import logging

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, encoding='utf-8', level=logging.DEBUG)
log = logging.getLogger(PurePath(__file__).name)


class Order:
    """
    An individual order details
    """
    side_flag_map = {True: "BUY", False: "SELL"}

    def __init__(self, side: bool, symbol: str, quantity: int, limit: float, close_market_when_done=False):
        """
        :param self: Represent the instance of the class
        :param side: bool: Determine whether the order is a buy or sell
        :param symbol: str: Identify the stock that is being traded
        :param quantity: int: Set the number of shares to be bought or sold
        :param limit: float: Set the limit price for the order
        :param close_market_when_done: Determine whether the market should be closed when
            the order is executed
        :return: None
        """
        self.side = side
        self.symbol = symbol
        self.quantity = quantity
        self.limit = limit
        self.execution_price = 0
        self.execution_time = ""
        self.close_market_when_done = close_market_when_done
        log.debug("Order created: %s", self.format_order())

    def set_execution_price(self, execution_price: float):

        """
        The set_execution_price function preserves execution price for executed orders.

        :param self: Represent the instance of the class
        :param execution_price: float:
        :return:
        """
        self.execution_price = execution_price

    def set_execution_timestamp(self):
        """
        The set_execution_timestamp function calculates the time stamp for when the
        function is executed.

        :param self: Represent the instance of the class
        :return: The time stamp
        """
        self.execution_time = "{:%H:%M:%S}".format(datetime.now())

    def format_order(self):
        """
        The format_order function is used to format the order details for screen output.
        The function returns a string that contains the side, quantity, symbol, limit and
        state of an order.

        :param self: Represent the instance of the class
        :return: A string
        """
        state = "OPEN"
        if self.execution_price:
            state = f"(EXECUTED - {self.execution_price:.2f})"
        return (f"[{Order.side_flag_map[self.side]} {self.quantity:,} "
                f"{self.symbol} @ {self.limit:,.2f}] {state}")
