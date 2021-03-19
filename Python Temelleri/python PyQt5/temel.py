import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('İlk Uygulama.')  # pencereye başlık ekler.
        self.setGeometry(200, 200, 600, 600)  # konumunu ve boyutunu ayarlar.
        # pencereye sol üst köşesine icon ekler.
        self.setWindowIcon(QIcon("icon.png"))
        # pencere üzerindeki fare imlecine yazı ekler.
        self.setToolTip("my tooltip")

        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız : ")
        self.lbl_name.move(20, 10)  # Adınız labelini konumlandırır.

        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Soyadınız : ")
        self.lbl_name.move(20, 50)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(150, 150)
        self.lbl_result.move(100, 80)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(60, 15)
        self.txt_name.resize(150, 30)  # text_box boyutunu ayarlar.

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(75, 55)
        self.txt_surname.resize(150, 30)

        self.btn_name = QtWidgets.QPushButton(self)
        self.btn_name.setText("Button")
        self.btn_name.move(100, 100)
        self.btn_name.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_result.setText(
            'Ad:' + self.txt_name.text() + ' Soyad:'+self.txt_surname.text())


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
