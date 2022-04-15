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

prices_df = pd.read_csv(PRICES)
prices_df = prices_df.set_index('Date')
prices_df = prices_df.sort_index(ascending=True)
print(prices_df.head())

ticker = 'MMM'
sharpe = get_sharpe(ticker, prices_df[ticker])

