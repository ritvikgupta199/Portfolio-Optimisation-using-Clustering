from traceback import print_tb
import numpy as np
import pandas as pd
import os
import argparse

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import discrete_allocation
from pypfopt import risk_models
from pypfopt import expected_returns


def get_mean_var_wts(prices):
    mu = expected_returns.mean_historical_return(prices)
    sigma = risk_models.sample_cov(prices)
    ef = EfficientFrontier(mu, sigma, weight_bounds=(0,1))
    portfolio = ef.min_volatility()
    pf_wt = ef.clean_weights()
    return pf_wt

def write_wts(filename, wts):
    print(f'The weights for {filename} are as follows:')
    fw = open(filename, 'w')
    for idx, wt in wts.items():
        print(f'{idx}, {wt}')
        fw.write(f'{idx}, {wt}\n')
    print('\n')
    fw.close()

parser = argparse.ArgumentParser('max_sharpe')
parser.add_argument('--year', type=int, help='Year')
parser.add_argument('--quarter', type=int, help='Quarter')

args = parser.parse_args()

PRICES = '../data/prices/prices_' + str(args.year) + 'q' + str(args.quarter) + '.csv'
TICKER_FILE = 'portfolios/portfolio_shortlist.csv'
SNP_LIST = '../snp500sym.csv'
PORTFOLIO_BM = 'portfolios/portfolio_bm.csv'
PORTFOLIO_ALL = 'portfolios/portfolio_all.csv'

snp_list = open(SNP_LIST, 'r').readlines()
# tickers_all = [snp_list[int(ticker)].strip() for ticker in np.arange(200, 300)]
tickers_bm = [ticker.strip() for ticker in open(TICKER_FILE, 'r').readlines()]

prices_df = pd.read_csv(PRICES)
prices_df = prices_df.set_index('Date')

prices_bm = prices_df[tickers_bm]
bm_wts = get_mean_var_wts(prices_bm)
write_wts(PORTFOLIO_BM, bm_wts)

# prices_all = prices_df[tickers_all]
# all_wts = get_mean_var_wts(prices_all)
# write_wts(PORTFOLIO_ALL, all_wts)