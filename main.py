import random
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QPainter, QColor


class Circle(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 500, 500, 500)
        self.setWindowTitle('Random yellow circles')
        self.button = QPushButton('Нарисовать', self)
        self.button.move(200, 250)
        self.button.resize(100, 50)
        self.draw_flag = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.draw_flag = True
        self.repaint()

    def draw(self, qp):
        a = random.randint(10, 100)
        r = 255
        g = 255
        b = 0
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
