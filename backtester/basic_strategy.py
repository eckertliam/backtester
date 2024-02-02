import backtrader as bt


class BasicStrategy(bt.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data)
        self.ema = bt.indicators.ExponentialMovingAverage()

        close_over_sma = self.data.close > self.sma
        close_over_ema = self.data.close > self.ema

        self.buy_sig = bt.indicators.CrossOver(close_over_sma, close_over_ema)

    def next(self):
        self.log('Close, %.2f' % self.data.close[0])

        if self.buy_sig > 0:
            self.log('BUY CREATE, %.2f' % self.data.close[0])
            self.buy()
        elif self.buy_sig < 0:
            self.log('SELL CREATE, %.2f' % self.data.close[0])
            self.sell()



