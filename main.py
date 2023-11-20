import random
from PyQt5 import uic
import sys
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('круг.ui', self)
        self.btn.clicked.connect(self.paint)
        self.a = False

    def paint(self):
        self.a = True
        self.update()

    def paintEvent(self, event):
        if self.a:
            qp = QPainter(self)
            qp.setBrush(QColor(255, 219, 139))
            m = random.randint(20, 501)
            qp.drawEllipse(int(500 - m / 2), int(500 - m / 2), m, m)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    ex.show()
    sys.exit(app.exec())
