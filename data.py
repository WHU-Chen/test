import numpy as np
import random
import matplotlib.pyplot as plt
import IPython

for n in range(7, 20):
    X = np.arange(0)
    Y = np.arange(0)
    for i in range(n):
        x = random.uniform(0, 10000)
        y = random.uniform(0, 10000)
        X = np.hstack((X, x + np.random.normal(-50, 100, 100)))
        Y = np.hstack((Y, y + np.random.normal(-50, 100, 100)))
    if n == 9:
        plt.scatter(X, Y)
        plt.show()
    with open('out%d.txt' % (i,),'w') as f:
        for i in range(len(X)):
            f.write('%d\t%d\n' % (X[i], Y[i]))


