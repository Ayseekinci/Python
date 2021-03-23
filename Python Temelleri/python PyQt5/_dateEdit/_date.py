import sys
from PyQt5 import QtWidgets
from _dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculatee)

    def calculatee(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEdit_2.date()
        print(start, end)

        print('Days in Month : {0}'.format(start.daysInMonth()))
        print('Days in Month : {0}'.format(start.daysInYear()))
        print('Total Days : {0}'.format(start.daysTo(end)))

        now = QDate.currentDate()
        print('Total Days From Now : {0}'.format(start.daysTo(now)))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()
