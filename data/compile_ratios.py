syms = []
symfile = open('snp500sym.csv','r')
symline = symfile.readline()
while symline:
    syms.append(symline.strip())

ratois = open('ratios.json','w')
