""" Order Book object definition """
import logging
from pathlib import PurePath
from .order import Order
from .position import Position

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT, encoding="utf-8", level=logging.DEBUG)
log = logging.getLogger(PurePath(__file__).name)


class OrderBook:
    """Collection of orders, executed orders and resulting positions"""

    def __init__(self):
        """
        Represents a collection of the following attributes

        orders -- dictionary of symbols pointing to a list of orders
        completed_orders -- all completed orders are put in a single list
        positions -- netted and there should be one positions per symbol

        :param self: Represent the instance of the class
        :return: New object
        """
        self.orders = {}
        self.completed_orders = []
        self.positions = {}

    def add_order(self, side, symbol, quantity, limit):
        """
        The add_order function takes in a side, symbol, quantity and limit.
        It then creates an order object with the given parameters.
        If the symbol is not already in self.orders it adds it to self.orders
        as a key with an empty list as its value (value TBD).
        Finally, it appends the order to that symbols list of orders and returns that order.

        :param self: Represent the instance of the class
        :param side: Determine whether the order is a buy or sell
        :param symbol: Identify the stock that is being traded
        :param quantity: Determine how many shares of a stock the user wants to buy or sell
        :param limit: Set the limit price of an order
        :return: The order that was just added
        """
        order = Order(side, symbol, quantity, limit)
        if symbol not in self.orders:
            self.orders[symbol] = []
        self.orders[symbol].append(order)
        return order

    def exec_order(self, order: Order, execution_price):
        """
        The exec_order function is used to move an order from the book to the executed orders list.
        It also updates the position of a stock if it exists, or creates a new position for that stock.

        :param self: Refer to the object itself
        :param order: Order: Pass the order object to the function
        :param execution_price: Set the execution price of the order
        :return: The completed_orders list, which is a list of all the orders that have been executed
        """
        order.set_execution_price(execution_price)
        order.set_execution_timestamp()
        if order.symbol not in self.positions:
            self.positions[order.symbol] = Position(order.symbol)
        self.positions[order.symbol].amend_position(order)
        self.completed_orders.append(order)
        self.orders[order.symbol].remove(order)

    def check_tick(self, symbol, bid, ask):
        """
        The check_tick function is called every time a new tick comes in and is used as
        the callback function.

        It checks the bid and ask prices against the limit price of each order,
        and if they are within range, it executes that order.
        The execution_client then sends an instruction to buy or sell at that price.

        # Given a tick, will compare to available orders in list

        :param self: Refer to the object itself
        :param symbol: Check the orders dictionary for a symbol
        :param bid: Compare the bid price to the order limit
        :param ask: Compare the ask price to the limit price of an order
        :return: Nothing
        """
        if symbol not in self.orders:
            return
        for order in self.orders[symbol]:
            if not order:
                continue
            if order.side:
                if ask <= order.limit:
                    log.debug(
                        "EXECUTION: BUY Order: ask (%s) is below order_execution (%s)",
                        ask,
                        order.limit,
                    )
                    self.exec_order(order, ask)
                    # self.execution_client.buy(symbol, order.quantity)
            else:
                if bid >= order.limit:
                    log.debug(
                        "EXECUTION: SELL Order: bid (%s) is above order_execution (%s)",
                        ask,
                        order.limit,
                    )
                    self.exec_order(order, bid)
                    # self.execution_client.sell(symbol, order.quantity)

    def print_all(self, verbiage):
        """
        The print_all function will dump all the available data to stdout formatted as output.

        :param self: Refer to the object itself
        :param verbiage: Should be used to identify book name
        :return: None
        """
        print("\n\n========= BOOK [%s] ===========" % verbiage)
        self.print_order_book()
        self.print_completed_order_book()
        self.print_positions()

    def print_order_book(self):
        """
        The print_order_book function prints all orders from the dictionary.
        It iterates through each key in the dictionary and then iterates through each order in that list of orders.
        If there is an order, it will print out a formatted version of that order.

        :param self: Refer to the object itself
        :return: All the orders from the dictionary
        """
        print("\nOrders:")
        for key, orders in self.orders.items():
            for order in orders:
                if order:
                    print("\t" + order.format_order())

    def print_completed_order_book(self):
        """
        The print_completed_order_book function prints the completed orders in a formatted way.
            It takes no arguments and returns nothing.

        :param self: Reference the object that is calling the function
        :return: A list of completed orders
        """
        print("\nCompleted Orders:")
        for order in self.completed_orders:
            print("\t" + order.format_order())

    def print_positions(self):
        """
        The print_positions function prints out the positions of the portfolio.
        It takes no arguments and returns nothing. It simply prints out a list of all
        the positions in the portfolio, along with their current value.

        :param self: Access the attributes of the class
        :return: A string with the positions and total value of the portfolio
        """
        tot = 0
        print("\nPositions:")
        for symbol, position in self.positions.items():
            print("\t" + position.format_position())
            tot += position.net_value
        print("\nTotal value: ${VAL:,.2f}".format(VAL=tot))

    def get_qty_orders(self):
        """
        The get_qty_orders function returns the number of orders in the order list.

        :param self: Represent the instance of the class
        :return: The number of orders in the list
        """
        return len(self.orders)

    def get_completed_qty_orders(self):
        """
        The get_completed_qty_orders function returns the number of completed orders in a given restaurant.

        :param self: Represent the instance of the class
        :return: The number of completed orders
        """
        return len(self.completed_orders)
