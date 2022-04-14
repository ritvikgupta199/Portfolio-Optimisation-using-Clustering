import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

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


val_x = []
val_y = []
for idx, row in prices_df.iterrows():
    val_x.append(idx)
    val = 0
    for ticker in tickers:
        val += row[ticker] * pf_dict[ticker]
    val_y.append(val)

plt.plot(val_x, val_y)
plt.show()