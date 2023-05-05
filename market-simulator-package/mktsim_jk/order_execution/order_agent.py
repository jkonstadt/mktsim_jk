from abc import abstractmethod
from typing import Protocol


class OrderAgent(Protocol):
    """ Enforce the price_check function signature """

    @abstractmethod
    def price_check(self, symbol: str, bid_price: float, ask_price: float):
        """
        Abstract method to implement and order agent

        :param symbol: id of the product that has a price change
        :param bid_price: the current bid price of hte product
        :param ask_price: the current ask price of hte product
        :return: None
        """
        raise NotImplementedError
