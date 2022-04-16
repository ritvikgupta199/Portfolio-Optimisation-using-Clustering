import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

def get_sharpe(ticker, prices_df):
    prices = prices_df[ticker]
    daily_rets = prices.pct_change()
    daily_rets = daily_rets.dropna()
    daily_rets = daily_rets.values
    avg_daily_ret = np.mean(daily_rets)
    std_daily_ret = np.std(daily_rets)
    sharpe = avg_daily_ret / std_daily_ret
    annual_sharpe = sharpe * np.sqrt(252)
    return annual_sharpe


PRICES = '../data/prices/prices_2021q2.csv'
TICKER_FILE = '../bm_points_covered_by_landmarks'
SNP_LIST = '../snp500sym.csv'
SELECT_FRAC = 0.1
SHORTLIST = 'portfolios/portfolio_shortlist.csv'

prices_df = pd.read_csv(PRICES)
prices_df = prices_df.set_index('Date')
prices_df = prices_df.sort_index(ascending=True)

snp_list = open(SNP_LIST, 'r').readlines()
fw = open(SHORTLIST, 'w')
for row in open(TICKER_FILE, 'r').readlines():
    tickers = row.strip().split(' ')
    tickers = [snp_list[int(ticker)-1].strip() for ticker in tickers]
    sharpe_dict = {}
    for ticker in tickers:
        sharpe_dict[ticker] = get_sharpe(ticker, pd.read_csv(PRICES))
    sharpe_df = pd.DataFrame(pd.DataFrame([{'ticker': k, 'sharpe': v} for k, v in sharpe_dict.items()]))
    sharpe_df = sharpe_df.set_index('ticker')
    sharpe_df = sharpe_df.sort_values('sharpe', ascending=False)
    (r, c) = sharpe_df.shape
    n = int(np.ceil(r * SELECT_FRAC))
    selected_tickers = sharpe_df.head(n).index.values
    fw.write(', '.join(selected_tickers) + '\n')
fw.close()

