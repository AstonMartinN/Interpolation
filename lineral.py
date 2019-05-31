import scipy.linalg as sla
import numpy as np

def get_value(X1, X2, Y1, Y2, Z):
    ans = (Y2 - Y1)/(X2 - X1)
    ans = ans * (Z - X1)
    return ans + Y1

def serch(X, Z, n):
    for i in range(n):
        if Z > X[i]:
            return i
    return -1


#n = int(input())
#x = np.array(list(map(int, input().split())))
#y = np.array(list(map(int, input().split())))
#n2 = int(input())
#z = np.array(list(map(int, input().split())))
f = open('data/train.dat')
g = open('data/train.ans')
t = open('data/test.dat')
x = np.array(list(map(float, f.read().split())))
y = np.array(list(map(float, g.read().split())))
z = np.array(list(map(float, t.read().split())))
ans = open('data/test.ans', 'w')

for i in range(z.size):
    k = serch(x, z[i], x.size)
    if k < 0:
        print("NO DATA")
        continue
    else:
        #print(get_value(x[k], x[k+1], y[k], y[k+1], z[i]))
        ans.write( str(get_value(x[k], x[k+1], y[k], y[k+1], z[i])) + ' '  )
