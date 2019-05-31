import sys, random, math
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(0, 0, 120, 120)
        self.setWindowTitle('Points')
        self.show()
        self.x
        self.y


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    #def mousePressEvent(self, event):
        #print(event.pos().x())
        #print(event.pos().y())
        
    def drawPoints(self, qp):
        qp.setPen(QColor(0, 0, 255))
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
