import numpy as np
import pandas as pd
import os

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import discrete_allocation
from pypfopt import risk_models
from pypfopt import expected_returns

PRICES = '../prices.csv'
TICKER_FILE = 'tickers/tickers.csv'
tickers = [ticker.strip() for ticker in open(TICKER_FILE, 'r').readlines()]

prices_df = pd.read_csv(PRICES)
prices_df = prices_df.set_index('Date')
prices_df = prices_df[tickers]
print(prices_df.head())

