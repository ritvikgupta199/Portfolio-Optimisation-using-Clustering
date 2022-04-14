import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import os

PF_COST = 10000
EVAL_PRICES = '../data/prices/prices_2020q3.csv'
PORTFOLIO = 'portfolios/portfolio.csv'
tickers = []
pf_dict = {}
fr = open(PORTFOLIO, 'r')
for line in fr.readlines():
    tokens = line.split(',')
    tickers.append(tokens[0].strip())
    pf_dict[tokens[0]] = float(tokens[1])

prices_df = pd.read_csv(EVAL_PRICES)
prices_df = prices_df.set_index('Date')
prices_df = prices_df[tickers]

sp500_df = web.DataReader('sp500', start = prices_df.index.min(), end = prices_df.index.max(), data_source='fred')
sp500_qt = PF_COST / sp500_df.loc[prices_df.index.max()]['sp500']

val_x, val_pf, val_sp = [], [], []
for idx, row in prices_df.iterrows():
    val_x.append(idx)
    val = 0
    for ticker in tickers:
        val += row[ticker] * pf_dict[ticker]
    val_pf.append(val)
    val_sp.append(sp500_df.loc[idx]['sp500']*sp500_qt)

plt.plot(val_x, val_pf)
plt.plot(val_x, val_sp)
plt.show()