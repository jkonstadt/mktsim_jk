""" Market simulation with asyncio """
import asyncio
import logging
from datetime import datetime
from pathlib import PurePath
from random import randrange, seed

seed()

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT, encoding="utf-8", level=logging.DEBUG)
log = logging.getLogger(PurePath(__file__).name)


class MarketPublisher:
    """
    Market data simulator (bid/ask).
    All the symbols in the market open dictionary will move according to
    market_direction
    """

    def __init__(self, market_open=None, market_direction=1, next_quote_delay=1,
                 price_check_callback=None, output=False):
        """
         Sets up market to publish in specified direction with a specified delay 
         between tick. This is useful for printing to standard output ( default ) or 
         to get a list of quotes that can be used to create a market
         
         :param market_open: Market open ( default : None )
         :param market_direction: Direction of market ( default : 1 )
         :param next_quote_delay: Delay between next quote ( default : 1 )
         :param price_check_callback: Function to call on tick
         :param output: Set to True for printing to
        """
        self.market_direction = market_direction
        self.next_quote_delay = next_quote_delay
        self.market_open = {"IBM": 100} if not market_open else market_open
        self.market_quote = {}
        self.price_check_callback = price_check_callback
        self.output = output
        self.status = True

    def is_open(self):
        """
        The is_open function checks the status of the door.
            If it is open, then it returns True.
            If it is closed, then it returns False.

        :param self: Refer to the instance of the class
        :return: The status of the door
        """
        return self.status

    def set_callback(self, callback):
        """
        Used to set the callback function when a price tick is updated.
        The callback should take two arguments: current price tick and new price.

        Currently implemented as a single call back for an order. This would
        need to be expanded to a set of callbacks.

        :param self: Represent the instance of the class
        :param callback: Set the function to be called when price tick is updated
        :return: Nothing
        """
        self.price_check_callback = callback

    async def schedule_close(self, seconds_til_close=5):
        """
        The schedule_close function is used to schedule the closing of a market.
        It takes in an optional parameter, seconds_til_close, which defaults to 5 if not specified.
        The function then sleeps for the number of seconds specified by this parameter and closes
        the market by setting its status attribute to False.

        Schedule close of market by setting status to False for Market. Closes market by
        setting status to False

        :param self: Represent the instance of the object itself
        :param seconds_til_close: Set the amount of time until the market closes
        :return: The close_market function
        """
        log.info("Seconds until market closes: %d", seconds_til_close)
        await asyncio.sleep(seconds_til_close)
        self.close_market()

    def close_market(self):
        """
        Mark market as closed. Will prevent future executions.

        Until other market sessions are added, of course ...
        """
        self.status = False

    async def get_market(self):
        """
        Moves BIDs for all stocks according to market_direction. Once new BID is
        calculated, will set ASK based on spread
        Prices fluctuate up to $2 (tic size = $0.25)

        Get Market Quote based on market_direction and next_quote_delay This is a
        generator function that iterates through all open market quotes and calls
        move_market and set_market
        """
        spread = randrange(1, 5) / 4
        await asyncio.sleep(self.next_quote_delay)
        for symbol in self.market_open.keys():
            # Move BID
            self.move_market(symbol)
            # Set ASK based on random spread
            self.market_quote[symbol][1] = self.market_quote[symbol][0] + spread
            if self.output:
                time_stamp = "{:%H:%M:%S}".format(datetime.now())
                bid = self.market_quote[symbol][0]
                ask = self.market_quote[symbol][1]
                print(f"{time_stamp:8s} - {symbol:<8} {bid:7.2f} | {ask:7.2f}")
            if self.price_check_callback:
                self.price_check_callback(
                    symbol, self.market_quote[symbol][0], self.market_quote[symbol][0]
                )

    def move_market(self, symbol):
        """
        Moves the market according to market_direction. This is a function
        to be called from Market.

        price adjust creates spread of +- $1.00 with ticks of $0.25

        :param symbol: The symbol we want to
        """
        price_adjust = randrange(1, 9, 1) / 4 * self.market_direction

        if symbol not in self.market_open:
            raise ValueError("Symbol not listed in market")
        if symbol not in self.market_quote:
            self.market_quote[symbol] = [None, None]
            self.market_quote[symbol][0] = self.market_open[symbol]
        else:
            self.market_quote[symbol][0] += price_adjust

    async def start_publishing(self):
        """
        The start_publishing function is the main function of this class. It creates a
        task to schedule the market close, and then it enters an infinite loop that waits
        for price changes on a symbol and prints them out in real time. The loop will
        only exit when the market closes.

        :param self: Represent the instance of the class
        :return: True when the market is closed
        """
        asyncio.create_task(self.schedule_close())
        if self.output:
            print("TIME       TICKER       BID |     ASK")
            print("--------   -------- ------- | -------")
        while self.is_open():
            # While market is open, wait for price change on symbol
            mkt = asyncio.create_task(self.get_market())
            await mkt

        return True

    async def wait_until_close(self):
        """
        Wait until the connection is closed. This is useful for tests that need to know
        when to stop and wait for the connection to close and perform post close actions

        :returns: True if the connection is closed False otherwise. Note that it may return
        False in the event of an error
        """
        while self.is_open():
            await asyncio.sleep(1)
        return True


def main():
    """
    This is the main function of the MarketPublisher. It creates a MarketPublisher
    instance and starts publishing.

    Without any hooks, this will simply  start moving the market, and optionally printing
    to the screen.
    """
    market = MarketPublisher(market_open={"IBM": 102}, market_direction=-1, output=True)
    asyncio.run(market.start_publishing())


if __name__ == "__main__":
    main()
