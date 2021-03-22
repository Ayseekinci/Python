import sys
from PyQt5 import QtWidgets
from _comboboxForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.cbSehirler
        combo.addItem('İstanbul')
        combo.addItem('Ankara')
        combo.addItem('Adıyaman')
        combo.addItem('Malatya')
        combo.addItems(['İzmir', 'Elazığ', 'Samsun', 'Kayseri'])

        self.ui.BtnLoadItems.clicked.connect(self.LoadItems)
        self.ui.BtnGetItem.clicked.connect(self.GetItem)

    def LoadItems(self):
        sehirler = ['Muğla', 'Adana', 'Kilis', 'Mersin']
        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        print(self.ui.cbSehirler.currentIndex())
        print(self.ui.cbSehirler.currentText())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()
