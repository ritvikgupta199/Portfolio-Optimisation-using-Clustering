from tqdm import tqdm
import requests
import time
import os
import json

API_KEY = open('api_key.txt', 'r').readlines()[0].strip()
DIR = '../data/'
TICKER_LIST = '../snp500sym.csv'
FUNCTION = 'CASH_FLOW'

path = os.path.join(DIR, FUNCTION)

if not os.path.exists(path):
    os.makedirs(path)
    print(f'Created directory {path}')

def get_data(function, ticker):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={API_KEY}'
    r = requests.get(url)
    return r.json()


f = open(TICKER_LIST, 'r')
for line in tqdm(f.readlines()):
    ticker = line.strip()
    filename = os.path.join(path, ticker + '.json')
    if os.path.exists(filename):
        data = json.load(open(filename, 'r'))
        if len(data.keys()) != 1:
            continue
    data = get_data(FUNCTION, ticker)
    json.dump(data, open(filename, 'w'), indent=4)
    time.sleep(12)
