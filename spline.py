import scipy.linalg as sla
import numpy as np

def running(A, B, C, F, N):
    alpha = np.empty(N + 1)
    beta = np.empty(N + 1)
    alpha[0] = 0
    beta[0] = 0
    for i in range(0, N):
        d = A[i]*alpha[i] + B[i]
        alpha[i + 1] = (-1 * C[i]) / d
        beta[i + 1] = (F[i] - A[i]*beta[i]) / d
    X = np.empty(N + 1)
    X[N] = 0
    for i in range(0, N):
        X[N - i - 1] = alpha[N - i]*X[N - i] + beta[N - i]
    return X

def generateSpline(X, Y, A, B, C, D):
    n = X.shape[0] - 1
    h = (X[n] - X[0]) / n
    a = np.array([1] + [1] * (n - 1) + [0])
    b = np.array([1] + [4] * (n - 1) + [1])
    c = np.array([0] + [1] * (n - 1) + [1])
    f = np.zeros(n + 1)
    for i in range(1 ,n):
        f[i] = 3 * (Y[i -1] - 2 * Y[i] + Y[i + 1]) / h**2
    s = running(a, b, c, f, a.size)
    for i in range(0, n):
        B[i] = s[i]
    for i in range(0, n - 1):
        A[i] = (B[i + 1] - B[i]) / (3*h)
        C[i] = (Y[i + 1] - Y[i])/h - (B[i + 1] + 2 * B[i])*(h/3)
        D[i] = Y[i]
    A[n - 1] = (0 - B[n - 1]) / (3*h)
    C[n - 1] = (Y[i + 1] - Y[i])/h - (2 * B[n - 1])*(h/3)
    D[n - 1] = Y[n - 1]

def value(Z, X, A, B, C, D):
    return A*((Z - X)**3) + B*((Z - X)**2) + C*(Z - X) + D




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




A = np.empty(x.size - 1);
B = np.empty(x.size - 1);
C = np.empty(x.size - 1);
D = np.empty(x.size - 1);
generateSpline(x, y, A, B, C, D)
for i in range(z.size):
    k = -1
    for j in range(x.size):
        if z[i] > x[j]:
            k = j
    if k < 0:
        print("ERROR")
    else:
        #print(value(z[i], x[k], A[k], B[k], C[k], D[k]))
        ans.write(str( value(z[i], x[k], A[k], B[k], C[k], D[k]) ) + ' ')










