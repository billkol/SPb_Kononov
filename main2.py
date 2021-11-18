import sys
from PyQt5.QtGui import QPainter, QPaintEvent, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 141, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "зелёный круг"))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.painting = False
        self.pushButton.clicked.connect(self.startPaint)

    def startPaint(self):
        self.painting = True
        self.update()

    def paintEvent(self, event: QPaintEvent):
        if self.painting:
            paint = QPainter()
            paint.begin(self)
            self.draw(paint)
            paint.end()
            self.painting = False

    def draw(self, qp: QPainter):
        self.a = random.randrange(10, 200)
        self.x = random.randrange(10, 200)
        self.y = random.randrange(10, 200)
        qp.setBrush(
            QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        qp.drawEllipse(self.x, self.y, self.a, self.a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = Window()
    wndw.show()
    app.exec()
