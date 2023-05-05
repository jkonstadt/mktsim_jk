.. documentation master file, created by
   sphinx-quickstart on Wed May  3 19:04:18 2023.

Welcome to Market Simulator (mktsim_jk) documentation!
=======================================================

mktsim_jk is an exercise to familiarize myself with various libraries and
functions including asyncio and abstract typing to create a concurrently executing
market data simulator.

The project is to create a simplified object library that will create a moving 
market in a specified direction. When the market move, events are passed to the
order book, which will execute limit order that become marketable.

The order book tracks executed orders and aggregates positions as the orders
complete.

Check out the :doc:`usage` section for further information, as well as
:doc:`testing` for more details on implementation.

.. toctree::
   :maxdepth: 4
   :caption: Contents:

modules
generated

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Contents
========

.. toctree::
   usage
   testing
   modules
   license



