import sys, random, math
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
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



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 200, 200)
        self.setWindowTitle('Points')
        self.show()
        self.my_x = []
        self.my_y = []
        self.count = 0

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        #self.drawLine(qp)
        #print(self.my_x.shape[0])
        #print(self.size().width())
        #print(self.count)
        #print(self.my_x)
        if self.count > 3:
            A1 = np.zeros(self.count - 1)
            B1 = np.zeros(self.count - 1)
            C1 = np.zeros(self.count - 1)
            D1 = np.zeros(self.count - 1)
            A2 = np.zeros(self.count - 1)
            B2 = np.zeros(self.count - 1)
            C2 = np.zeros(self.count - 1)
            D2 = np.zeros(self.count - 1)
            T = np.array(range(self.count))
            generateSpline(T, np.array(self.my_x), A1, B1, C1, D1)
            generateSpline(T, np.array(self.my_y), A2, B2, C2, D2)
            self.drawLine(qp, A1, B1, C1, D1, A2, B2, C2, D2, T)
        qp.end()

    def mousePressEvent(self, event):
        self.my_x.append(event.pos().x())
        self.my_y.append(event.pos().y())
        self.count = self.count + 1
        self.update()

    def drawLine(self, qp, A1, B1, C1, D1, A2, B2, C2, D2, T):
        for I in range(1000):
            i = ((self.count  - 1 )/ (1000) )* I
            k = 0
            for j in range(self.count):
                if i < T[j]:
                    k = T[j] - 1
                    break
            #print(k, A1.size, self.count, i, T.size)
            XX = value(i, k, A1[k], B1[k], C1[k], D1[k])
            YY = value(i, k, A2[k], B2[k], C2[k], D2[k])
            qp.drawPoint(XX, YY)
            #print(XX, YY)

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()
        N = 100000
        for i in range(N):
            x = (size.width()/N)*i
            qp.drawPoint(x, x)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
