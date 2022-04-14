import json

syms = []
dates = []
prices = []
symfile = open('snp500sym.csv','r')
symline = symfile.readline()
while symline:
    syms.append(symline.strip())
    symline = symfile.readline()

# syms = syms[:3]

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

f = open('prices.csv','w')
f.write('Date,')
for sym in syms:
    f.write(sym+',')
f.write('\n')
for i in range(len(dates)):
    f.write(dates[i]+',')
    for j in range(len(prices)):
        if i >= len(prices[j]):
            continue
        f.write(str(prices[j][i])+',')
    f.write('\n')
