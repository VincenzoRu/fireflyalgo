# backtest.py

"""
Backtest module
"""

from abc import ABCMeta, abstractmethod
import pandas_datareader.data as web #requires 'pip install' on the command line
import quandl as qdl #requires 'pip install' on the command line
import pandas as pd
import numpy as np
import classes.firefly as ff

#Data handler
class DataHandler:
    """
    Requires:
    option - Option varies from A and B.
        A for Quandl module and
        B for Pandas datareader module
    symbol - A stock symbol on which to form a strategy on.
    start - Start of timeframe
    end -  End of timeframe
    """

    def __init__(self, option, symbol, start, end):
        self.option = option
        self.symbol = symbol
        self.start = start
        self.end = end

    def generate_data(self):
        """Generate the data from selected option"""
        print("Generating data")
        if self.option == "A":
            print("option A selected. Quandl")
            data = qdl.get("WIKI/%s" % self.symbol, start_date=self.start, end_date=self.end)
        elif self.option == "B":
            print("option B selected. Pandas Datareader")
            data = web.DataReader(self.symbol, "iex", self.start, self.end)
        return data

    def format_data(self):
        """Clean and formats the data"""
        print("Formats data")

#Optimization - abstract
class Optimizer(object):
    """Optimizer is a..."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def optimize_signals(self):
        """An implementation is required to return the DataFrame of symbols
        containing the optimized signals to go long, short or hold (1, -1 or 0)."""
        raise NotImplementedError("Should implement generate_signals()!")

#Strategy - abstract
class Strategy(object):
    """Strategy is an abstract base class providing an interface for
    all subsequent (inherited) trading strategies.

    The goal of a (derived) Strategy object is to output a list of signals,
    which has the form of a time series indexed pandas DataFrame.

    In this instance only a single symbol/instrument is supported."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_signals(self):
        """An implementation is required to return the DataFrame of symbols
        containing the signals to go long, short or hold (1, -1 or 0)."""
        raise NotImplementedError("Should implement generate_signals()!")

#Portfolio - abstract
class Portfolio(object):
    """An abstract base class representing a portfolio of
    positions (including both instruments and cash), determined
    on the basis of a set of signals provided by a Strategy."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_positions(self):
        """Provides the logic to determine how the portfolio
        positions are allocated on the basis of forecasting
        signals and available cash."""
        raise NotImplementedError("Should implement generate_positions()!")

    @abstractmethod
    def backtest_portfolio(self):
        """Provides the logic to generate the trading orders
        and subsequent equity curve (i.e. growth of total equity),
        as a sum of holdings and cash, and the bar-period returns
        associated with this curve based on the 'positions' DataFrame.

        Produces a portfolio object that can be examined by
        other classes/functions."""
        raise NotImplementedError("Should implement backtest_portfolio()!")

#Performance

class FireFly(Optimizer):
    """
    Requires:
    """
    def __init__(self, parameters):
        self.parameters = parameters[0:6]

        self.totalsignals = parameters[6]
        self.weights = parameters[7]
        self.optimized_weights = self.main_algo()

    def main_algo(self):
        initFF = ff.InitFFAlgo(self.parameters)
        #optimized_weights = initFF.getOptWeights
        #return optimized_weights
        print("Success")


class SimpleMAStrategy(Strategy):
    """
    Requires:
    symbol - A stock symbol on which to form a strategy on.
    bars - A DataFrame of bars for the above symbol.
    window - Lookback period for simple moving average."""

    def __init__(self, symbol, bars, window=90):
        self.symbol = symbol
        self.bars = bars
        self.window = window

    def generate_signals(self):
        """Returns the DataFrame of symbols containing the signals
        to go long, short or hold (1, -1 or 0)."""
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = 0.0
        signals['price'] = self.bars['close']

        # Create the set of simple moving averages over the respective periods
        #signals['mavg'] = pd.rolling_mean(bars['Close'], self.window, min_periods=1)
        signals['mavg'] = self.bars['close'].rolling(window=self.window).mean()

        # Create a 'signal' (invested or not invested) when the close price is greater than the simple moving average
        signals['signal'] = np.where(signals['price'] > signals['mavg'], 1.0, 0.0)

        # Take the difference of the signals in order to generate actual trading orders
        signals['positions'] = signals['signal'].diff()

        return signals

class MACrossStrategy(Strategy):
    """
    Requires:
    symbol - A stock symbol on which to form a strategy on.
    bars - A DataFrame of bars for the above symbol.
    short_window - Lookback period for short moving average.
    long_window - Lookback period for long moving average."""

    def __init__(self, symbol, bars, short_window=30, long_window=50):
        self.symbol = symbol
        self.bars = bars

        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        """Returns the DataFrame of symbols containing the signals
        to go long, short or hold (1, -1 or 0)."""
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = 0.0
        signals['price'] = self.bars['close']

        # Create the set of short and long simple moving averages over the
        # respective periods
        signals['short_mavg'] = self.bars['close'].rolling(window=self.short_window).mean()
        signals['long_mavg'] = self.bars['close'].rolling(window=self.long_window).mean()

        # Create a 'signal' (invested or not invested) when the short moving average crosses the long
        # moving average, but only for the period greater than the shortest moving average window
        signals['signal'] = np.where(signals['short_mavg'] > signals['long_mavg'], 1.0, 0.0)

        # Take the difference of the signals in order to generate actual trading orders
        signals['positions'] = signals['signal'].diff()

        return signals

class EMAStrategy(Strategy):
    """
    Requires:
    symbol - A stock symbol on which to form a strategy on.
    bars - A DataFrame of bars for the above symbol.
    window - Lookback period for simple moving average."""

    def __init__(self, symbol, bars, window=10):
        self.symbol = symbol
        self.bars = bars
        self.window = window

    def generate_signals(self):
        """Returns the DataFrame of symbols containing the signals
        to go long, short or hold (1, -1 or 0)."""
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = 0.0
        signals['price'] = self.bars['close']

        # Create the set of simple moving averages over the respective periods
        #signals['mavg'] = pd.rolling_mean(bars['Close'], self.window, min_periods=1)
        signals['emavg'] = self.bars['close'].ewm(span=self.window, adjust=False).mean()

        # Create a 'signal' (invested or not invested) when the close price is greater than the simple moving average
        signals['signal'] = np.where(signals['price'] > signals['emavg'], 1.0, 0.0)

        # Take the difference of the signals in order to generate actual trading orders
        signals['positions'] = signals['signal'].diff()

        return signals

class MarketOnClosePortfolio(Portfolio):
    """Encapsulates the notion of a portfolio of positions based
    on a set of signals as provided by a Strategy.

    Requires:
    symbol - A stock symbol which forms the basis of the portfolio.
    bars - A DataFrame of bars for a symbol set.
    signals - A pandas DataFrame of signals (1, 0, -1) for each symbol.
    initial_capital - The amount in cash at the start of the portfolio."""

    def __init__(self, symbol, bars, totalsignals, weights, initial_capital=100000.0):
        self.symbol = symbol
        self.bars = bars
        self.totalsignals = totalsignals
        self.weights = weights
        self.initial_capital = float(initial_capital)
        self.positions = self.generate_positions()

    def generate_positions(self):
        positions = pd.DataFrame(index=self.totalsignals.index).fillna(0.0)
        self.totalsignals['sumsignal'] = self.weights[0]*self.totalsignals['signal1'] + self.weights[1]*self.totalsignals['signal2'] + self.weights[2]*self.totalsignals['signal3']
        self.totalsignals['totalsignal'] = np.where(self.totalsignals['sumsignal'] > 0.5, 1.0, 0.0)
        # Buy a 100 shares
        positions[self.symbol] = 100*self.totalsignals['totalsignal']
        return positions

    def backtest_portfolio(self):
        # Initialize the portfolio with value owned
        portfolio = pd.DataFrame(index=self.totalsignals.index).fillna(0.0)
        portfolio[self.symbol] = self.positions[self.symbol]*self.bars['close']
        pos_diff = self.positions.diff()

        # Add `holdings` to portfolio
        portfolio['holdings'] = (self.positions.multiply(self.bars["close"], axis=0)).sum(axis=1)
        # Add `cash` to portfolio
        portfolio['cash'] = self.initial_capital - (pos_diff.multiply(self.bars['close'], axis=0)).sum(axis=1).cumsum()
        # Add `total` to portfolio
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        # Add `returns` to portfolio
        portfolio['returns'] = portfolio['total'].pct_change()

        return portfolio
