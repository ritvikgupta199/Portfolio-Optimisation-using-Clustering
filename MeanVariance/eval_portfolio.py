from turtle import color
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

PF_AMOUNT = 10000
EVAL_PRICES = '../data/prices/prices_2019q1.csv'
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
prices_df = prices_df.sort_index(ascending=True)
prices_df = prices_df[tickers]

sp500_df = web.DataReader('sp500', start = prices_df.index.min(), end = prices_df.index.max(), data_source='fred')
sp500_qt = PF_AMOUNT / sp500_df.loc[prices_df.index.min()]['sp500']

dates, val_pf, val_sp = [], [], []
for idx, row in prices_df.iterrows():
    dates.append(idx)
    val = 0
    for ticker in tickers:
        val += row[ticker] * pf_dict[ticker]
    val_pf.append(val)
    val_sp.append(sp500_df.loc[idx]['sp500']*sp500_qt)


fig, ax = plt.subplots(figsize=(8, 6))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

ax.plot(dates, val_pf, color='red', label='Portfolio')
ax.plot(dates, val_sp, color='blue', label='S&P500 Index')

ax.set_xlabel("Date")
ax.set_ylabel("Value of Portfolio")
ax.set_title("Portfolio vs S&P500 Index")
ax.legend()

plt.show()