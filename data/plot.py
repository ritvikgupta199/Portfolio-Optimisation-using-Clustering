import matplotlib.pyplot as plt

for year in range(2017, 2020):
    for qtr in range(1, 5):
        period = f'{year}_Q{qtr}'
        period_file = open(f'/home/anshuman/Portfolio-Optimisation/data/QuarterlyRatiosCleanNormalised/{period}.csv', 'r')
        header = period_file.readline()
        lines = period_file.readlines()
        x = []
        y = []
        for line in lines:
            line = line.strip().split(',')
            print(line)
            x.append(float(line[1]))
            y.append(float(line[2]))
        plt.scatter(x, y)
        plt.show()
        plt.plot(y)
        plt.show()
        plt.plot(x)
        plt.show()