import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from _listForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # LOAD
        self.loadstudents()

        # ADD
        # ((yeni öğrenci ekleme))
        self.ui.btnAdd.clicked.connect(self.addStudent)

        # EDİT
        # ((Öğrenci Güncelleme))
        self.ui.btnEdit.clicked.connect(self.editStudent)

        # REMOVE
        # ((Öğrenci Sil.))
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        # UP
        # ((Öğrenciyi ismini bi üste taşı))
        self.ui.btnUp.clicked.connect(self.upStudent)

        # DOWN
        # ((Öğrenci ismini bi alta taşı))
        self.ui.btnDown.clicked.connect(self.downStudent)

        # SORT
        # ((Öğrencileri Sıralama))
        self.ui.btnSort.clicked.connect(self.sortStudent)

        # Exit
        # ((pencereyi kapatma))
        self.ui.pushButton_5.clicked.connect(self.close)

    def loadstudents(self):
        self.ui.ListItems.addItems(['Ayşe', 'Zeynep', 'Ahmet'])
        self.ui.ListItems.setCurrentRow(0)  # 0.indexteki seçili olsun.

    def addStudent(self):
        curretIndex = self.ui.ListItems.currentRow()
        text, ok = QInputDialog.getText(self, "New Student ", "Student Name")

        if ok and text is not None:
            self.ui.ListItems.insertItem(curretIndex, text)

    def editStudent(self):
        index = self.ui.ListItems.currentRow()
        item = self.ui.ListItems.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Student",
                                            "Student Name", QLineEdit.Normal, item.text())
            if ok and text is not None:
                item.setText(text)

    def removeStudent(self):
        index = self.ui.ListItems.currentRow()
        item = self.ui.ListItems.item(index)

        if item is None:
            return

        q = QMessageBox.question(
            self, "Remove Student ", "Öğrenciyi silmek istiyor musunuz??"+item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.ListItems.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.ListItems.currentRow()
        if index >= 1:
            item = self.ui.ListItems.takeItem(index)
            self.ui.ListItems.insertItem(index-1, item)
            self.ui.ListItems.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.ListItems.currentRow()
        if index <= self.ui.ListItems.count()-1:
            item = self.ui.ListItems.takeItem(index)
            self.ui.ListItems.insertItem(index+1, item)
            self.ui.ListItems.setCurrentItem(item)

    def sortStudent(self):
        self.ui.ListItems.sortItems()

    def close(self):
        quit()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()
