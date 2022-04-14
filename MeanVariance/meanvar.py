import numpy as np
import pandas as pd
import os

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import discrete_allocation
from pypfopt import risk_models
from pypfopt import expected_returns


PRICES = '../data/prices/prices_2020q2.csv'
TICKER_FILE = 'tickers/tickers.csv'
tickers = [ticker.strip() for ticker in open(TICKER_FILE, 'r').readlines()]

prices_df = pd.read_csv(PRICES)
prices_df = prices_df.set_index('Date')
prices_df = prices_df[tickers]

mu = expected_returns.mean_historical_return(prices_df)
sigma = risk_models.sample_cov(prices_df)

ef = EfficientFrontier(mu, sigma, weight_bounds=(0,1))
sharpe_pfolio=ef.min_volatility()
sharpe_pwt=ef.clean_weights()
print(f'The weights for min volatility are {sharpe_pwt}')

latest_prices = discrete_allocation.get_latest_prices(prices_df)
allocation_minv, rem_minv = discrete_allocation.DiscreteAllocation(sharpe_pwt, latest_prices, total_portfolio_value=10000).lp_portfolio()

print('The allocation is as follows:')
for key, val in allocation_minv.items():
    print(f'{key}, {val}')

