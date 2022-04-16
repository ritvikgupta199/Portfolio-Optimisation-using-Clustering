import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import vars

PF_AMOUNT = 10000
YEAR = vars.YEAR
QTR = vars.QTR
# increment qtr
if QTR == 4:
    QTR = 1
    YEAR += 1
else:
    QTR += 1
EVAL_PRICES = '../data/prices/prices_' + str(YEAR) + 'q' + str(QTR) + '.csv'
PORTFOLIO_BM = 'portfolios/portfolio_bm.csv'
PORTFOLIO_ALL = 'portfolios/portfolio_all.csv'

def get_tickers_wts(filename):
    tickers = []
    pf_wts = {}
    fr = open(filename, 'r')
    for line in fr.readlines():
        tokens = line.split(',')
        tickers.append(tokens[0].strip())
        pf_wts[tokens[0]] = float(tokens[1])
    return tickers, pf_wts

def get_prices_alloc(pf_wts, tickers, prices):
    prices_pf = prices[tickers]
    latest_prices = prices_pf.loc[prices_pf.index.min()]
    pf_alloc = {}
    for idx, wt in pf_wts.items():
        pf_alloc[idx] = (wt * PF_AMOUNT) / latest_prices[idx]
    return prices_pf, pf_alloc

def get_value(prices, tickers, pf_alloc):
    val = 0
    for ticker in tickers:
        val += prices[ticker] * pf_alloc[ticker]
    return val

tickers_bm, bm_wts = get_tickers_wts(PORTFOLIO_BM)
print(bm_wts)
tickers_all, all_wts = get_tickers_wts(PORTFOLIO_ALL)

prices_df = pd.read_csv(EVAL_PRICES)
prices_df = prices_df.set_index('Date')
prices_df = prices_df.sort_index(ascending=True)

prices_bm, bm_alloc = get_prices_alloc(bm_wts, tickers_bm, prices_df)
prices_all, all_alloc = get_prices_alloc(all_wts, tickers_all, prices_df)

sp500_df = web.DataReader('sp500', start = prices_df.index.min(), end = prices_df.index.max(), data_source='fred')
sp500_qt = PF_AMOUNT / sp500_df.loc[prices_df.index.min()]['sp500']

dates, val_bm, val_all, val_sp = [], [], [], []
for idx, row in prices_df.iterrows():
    dates.append(idx)
    val_bm.append(get_value(row, tickers_bm, bm_alloc))
    val_all.append(get_value(row, tickers_all, all_alloc))
    val_sp.append(sp500_df.loc[idx]['sp500']*sp500_qt)

fig, ax = plt.subplots(figsize=(8, 6))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

ax.plot(dates, val_bm, color='green', label='Portfolio using BM')
# ax.plot(dates, val_all, color='red', label='Portfolio using All')
ax.plot(dates, val_sp, color='blue', label='S&P500 Index')

ax.set_xlabel("Date")
ax.set_ylabel("Value of Portfolio")
ax.set_title("Portfolio vs S&P500 Index")
ax.legend()

plt.show()