from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pandas as pd
import backtrader as bt
import backtrader.feeds as btfeeds
from .basic_strategy import BasicStrategy


class BackTester:
    def __init__(self, datapath, strategy):
        self.dataframe = pd.read_csv(datapath,
                                     skiprows=0,
                                     header=0,
                                     parse_dates=True,
                                     index_col=0)
        self.cerebro = bt.Cerebro(stdstats=False)
        self.cerebro.addstrategy(strategy)
        self.data = btfeeds.PandasData(dataname=self.dataframe)
        self.cerebro.adddata(self.data)


    def run(self, start_cash=10000):
        self.cerebro.broker.set_cash(start_cash)

        self.cerebro.run()

        if plot:
            self.cerebro.plot(style='candlestick', path=plotpath)

        return self.cerebro.broker.getvalue()
