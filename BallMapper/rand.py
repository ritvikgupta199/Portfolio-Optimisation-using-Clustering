import numpy as np
f = open("data/rand.csv", "w")
for i in range(1000):
    towrite = [np.random.rand()*10 for _ in range(20)]
    towrite = [str(x) for x in towrite]
    towrite = ",".join(towrite)
    towrite += "\n"
    f.write(towrite)
f.close()