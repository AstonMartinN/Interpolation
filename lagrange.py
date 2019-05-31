import scipy.linalg as sla
import numpy as np




def phi(I, X, Y, Z):
    p = 1
    for j in range(X.size):
        if j == I:
            continue
        p = p * ( (Z - X[j])/(X[I] - X[j]) )
    return p

def P(Z, X, Y):
    s = 0
    for i in range(X.size):
        s = s + Y[i] * phi(i, X, Y, Z)
    return s

#x = np.array(list(map(float, input().split())))
#y = np.array(list(map(float, input().split())))
#z = np.array(list(map(float, input().split())))


f = open('data/train.dat')
g = open('data/train.ans')
t = open('data/test.dat')
x = np.array(list(map(float, f.read().split())))
y = np.array(list(map(float, g.read().split())))
z = np.array(list(map(float, t.read().split())))
ans = open('data/test.ans', 'w')


for i in range(z.size):
    #print(P(z[i], x, y))
    ans.write(str(P(z[i], x, y)) +  ' ')
