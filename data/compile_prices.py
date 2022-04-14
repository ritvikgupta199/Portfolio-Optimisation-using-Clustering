import json
from math import ceil

syms = []
dates = []
prices = []
symfile = open('snp500sym.csv','r')
symline = symfile.readline()
while symline:
    syms.append(symline.strip())
    symline = symfile.readline()

for sym in syms:
    prices.append([])
    try:
        f = open('data/TIME_SERIES_DAILY/'+sym+'.json','r')
        data = json.load(f)
        f.close()
        for record in data["Time Series (Daily)"]:
            prices[-1].append(float(data["Time Series (Daily)"][record]["4. close"]))
    except:
        pass

f = open('data/TIME_SERIES_DAILY/'+syms[0]+'.json','r')
data = json.load(f)
f.close()
for key, val in data["Time Series (Daily)"].items():
    dates.append(key)

f = open('data/prices/prices.csv','w')
f.write('Date,')
for sym in syms:
    f.write(sym+',')
f.write('\n')
for year in range(1999, 2023):
    for qtr in range(1, 5):
        f_ = open('data/prices/prices_'+str(year)+'q'+str(qtr)+'.csv','w')
        f_.write('Date,')
        for sym in syms:
            f_.write(sym+',')
        f_.write('\n')
# print(dates)
for i in range(len(dates)):
    year = int(dates[i][0:4])
    qtr = int(dates[i][5:7])
    qtr = ceil(qtr/3)
    # print(year, qtr)
    f_ = open('data/prices/prices_'+str(year)+'q'+str(qtr)+'.csv','a')
    f.write(dates[i]+',')
    f_.write(dates[i]+',')
    for j in range(len(prices)):
        if i >= len(prices[j]):
            prices[j].append("")
        f.write(str(prices[j][i])+',')
        f_.write(str(prices[j][i])+',')
    f.write('\n')
    f_.write('\n')