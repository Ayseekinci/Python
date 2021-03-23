import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from _tableFrom import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.LoadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowCount = self.ui.tableWidget.rowCount()
            print(rowCount)
            self.ui.tableWidget.insertRow(rowCount)
            self.ui.tableWidget.setItem(
                rowCount, 0, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(
                rowCount, 1, QTableWidgetItem(price))

    def LoadProducts(self):
        protucts = [
            {'name': 'Samsung S5', 'price': 2000},
            {'name': 'Samsung S6', 'price': 3000},
            {'name': 'Samsung S7', 'price': 4000}

        ]

        self.ui.tableWidget.setRowCount(len(protucts))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Name', 'Price'))
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)

        rowindex = 0
        for protuct in protucts:
            self.ui.tableWidget.setItem(
                rowindex, 0, QTableWidgetItem(protuct['name']))
            self.ui.tableWidget.setItem(
                rowindex, 1, QTableWidgetItem(str(protuct['price'])))
            rowindex += 1

        # self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('Samsung S5'))
        # self.ui.tableWidget.setItem(0, 1, QTableWidgetItem('2500'))
        # self.ui.tableWidget.setItem(1, 0, QTableWidgetItem('Samsung S6'))
        # self.ui.tableWidget.setItem(1, 1, QTableWidgetItem('3000'))
        # self.ui.tableWidget.setItem(2, 0, QTableWidgetItem('Samsung S7'))
        # self.ui.tableWidget.setItem(2, 1, QTableWidgetItem('3500'))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()
