from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pandas as pd
import backtrader as bt
import backtrader.feeds as btfeeds
from basic_strategy import BasicStrategy

import numpy as np

datapath = '../data/btc_data.csv'

dataframe = pd.read_csv(datapath,
                        skiprows=0,
                        header=0,
                        parse_dates=True,
                        index_col=0)


cerebro = bt.Cerebro(stdstats=False)

cerebro.addstrategy(BasicStrategy)

data = btfeeds.PandasData(dataname=dataframe)

cerebro.adddata(data)

# print starting cash
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

# print ending cash
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
