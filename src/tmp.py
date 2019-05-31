import scipy.linalg as sla
import numpy as np


f = open('train.dat')
a = np.array(list(map(int, f.read().split())))
print(a)
f.close()
