from traceback import print_tb
import numpy as np
import pandas as pd
import os

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import discrete_allocation
from pypfopt import risk_models
from pypfopt import expected_returns


PF_AMOUNT = 10000
PRICES = '../data/prices/prices_2021q1.csv'
TICKER_FILE = '../bm_landmarks'
SNP_LIST = '../snp500sym.csv'
PORTFOLIO = 'portfolios/portfolio.csv'

snp_list = open(SNP_LIST, 'r').readlines()
tickers = [snp_list[int(ticker)-1].strip() for ticker in np.arange(201, 301)]
# print(tickers)
# tickers = [snp_list[int(ticker)-1].strip() for ticker in open(TICKER_FILE, 'r').readlines()]

prices_df = pd.read_csv(PRICES)
prices_df = prices_df.set_index('Date')
prices_df = prices_df[tickers]

mu = expected_returns.mean_historical_return(prices_df)
sigma = risk_models.sample_cov(prices_df)

ef = EfficientFrontier(mu, sigma, weight_bounds=(0,1))
sharpe_pfolio=ef.min_volatility()
sharpe_pwt=ef.clean_weights()

print('The weights are as follows:')
fw = open(PORTFOLIO, 'w')
for idx, wt in sharpe_pwt.items():
    print(f'{idx}, {wt}')
    fw.write(f'{idx}, {wt}\n')

