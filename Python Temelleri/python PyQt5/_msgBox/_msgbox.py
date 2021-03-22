import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _msgboxForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showDialog)

    def showDialog(self):
        result = QMessageBox.warning(
            self, 'Close App', 'Are you sure?', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes Clicked')
            QtWidgets.qApp.quit()
        else:
            print('No Clicked')

        # msg = QMessageBox()
        # msg.setWindowTitle('Close Application')
        # msg.setText('Emin misiniz?')
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(
        #     QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)

        # msg.buttonClicked.connect(self.popup_button)
        # x = msg.exec_()
        # print(x)

        # def popup_button(self, i):
        #     print(i.text())

        #     if i.text() == 'Ok':
        #         print('Okey')
        #         QtWidgets.qApp.quit()
        #     elif i.text() == 'Cancel':
        #         print('Cancel..')
        #     else:
        #         print('Ignore..')


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()
