import readline


with open("BallMapper/data/boston.txt",'w') as po:
    with open("BallMapper/data/boston.csv",'r') as b1:
        line = b1.readline()
        # line = line.strip()
        while(line):
            line = line.split(',')
            po.write(' '.join(line[:]))
            po.write('\n')
            # val.write('\n')
            line = b1.readline()

