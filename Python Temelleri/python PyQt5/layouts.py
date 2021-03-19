import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palatte = self.palette()
        palatte.setColor(QPalette.Window, QColor(color))
        self.setPalette(palatte)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 600, 600)

    # renkleri yatay sırala
        #layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('yellow'))

    # renkleri dikey sırala
        #layout = QtWidgets.QHBoxLayout()
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('yellow'))
        # widget.setLayout(layout)

        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color('red'))
        hlayout1.addWidget(Color('blue'))
        hlayout1.addWidget(Color('yellow'))
        hlayout1.setSpacing(30)  # boşluk oluşturur.

        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color('green'))
        hlayout2.addWidget(Color('orange'))
        hlayout2.setSpacing(30)  # boşluk oluşturur.

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        widget = QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

        # layout = QtWidgets.QGridLayout()

        # layout.addWidget(Color("red"),0,0)
        # layout.addWidget(Color("blue"),0,1)
        # layout.addWidget(Color("blue"),1,0)
        # layout.addWidget(Color("yellow"),1,1)
        # layout.addWidget(Color("yellow"),2,0)
        # layout.addWidget(Color("blue"),2,1)
        # layout.addWidget(Color("blue"),3,0)
        # layout.addWidget(Color("yellow"),3,1)
        #widget = QWidget()
        # widget.setLayout(Layout)
        # self.setCentralWidget(widget)


def app():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())


app()
