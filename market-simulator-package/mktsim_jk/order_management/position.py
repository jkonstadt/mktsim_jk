""" Position netting object definition """
import logging
from pathlib import PurePath
from .order import Order

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, encoding='utf-8', level=logging.DEBUG)
log = logging.getLogger(PurePath(__file__).name)


class Position:
    """ _summary_
    Stores net position by symbol
    """
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.net_quantity = 0
        self.net_value = 0.0

    def amend_position(self, order: Order):
        """amend_position
        Will read order and will net value to appropriate position
        Args:
            order (Order): _description_
        """
        modifier = -1 if not order.side else 1
        self.net_quantity += order.quantity * modifier
        self.net_value += (order.quantity * order.execution_price * modifier)

    def format_position(self):
        """format_position
        Format attibutes of position as string
        Returns:
            _type_: _description_
        """
        return (
            f"| {self.symbol} | Net {self.net_quantity:+,}"
            f" Shrs, Val ${self.net_value:,.2f}"
        )
