import sys
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPaintEvent

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUi()

    def initUi(self):

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Git и случайные окружности')
        self.button = QPushButton('Нарисовать', self)
        self.button.move(200, 400)
        self.button.resize(100, 80)
        self.draw_flag = False
        self.button.clicked.connect(self.paint)

    def paint(self):

        self.draw_flag = True
        self.repaint()

    def paintEvent(self, event: QPaintEvent):

        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp: QPainter):

        a = randint(10, 300)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 225)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(randint(0, 500), randint(0, 500), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
