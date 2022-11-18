import sys
from random import randint

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, \
    QGridLayout, QPushButton, QStatusBar
from PyQt5.QtGui import QPainter, QColor, QPaintEvent

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)

        self.centre_widget = QWidget(MainWindow)
        self.centre_widget.setObjectName('centralwidget')

        self.gridLay = QGridLayout(self.centre_widget)
        self.gridLay.setObjectName('gridLayout')

        self.button = QPushButton(self.centre_widget)
        self.button.setObjectName('drawCircleBtn')

        self.gridLay.addWidget(self.button, 1, 0, 1, 1)
        self.canvas = QLabel(self.centre_widget)
        self.canvas.setText('')
        self.canvas.setObjectName('canvas')
        self.gridLay.addWidget(self.canvas, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centre_widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow',
                                             'Random yellow circles'))
        self.button.setText(_translate('MainWindow', 'Нарисовать'))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
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
        a = randint(10, 100)
        r = 255
        g = 255
        b = 0
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(randint(0, 200), randint(0, 200), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
