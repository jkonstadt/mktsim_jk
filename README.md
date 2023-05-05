# mktsim_jk

## Simplified Python market simulator for learning and testing

mktsim_jk is an exercise to familiarize myself with various libraries and functions including asyncio and abstract typing to create a concurrently executing market data simulator.

The project is to create a simplified object library that will create a moving market in a specified direction. When the market move, events are passed to the order book, which will execute limit order that become marketable.

The order book tracks executed orders and aggregates positions as the orders complete.

## Location

You will find the package under `./market-simulator-package`

## Test Script

You will find the tests in `./market-simulator-package/order_agent_limit_tests.py`

## Documentation

Rhe complete API documentation built with Sphinx 
using Read-the-docs style.

You will find the html in `./docs/build/html` 

