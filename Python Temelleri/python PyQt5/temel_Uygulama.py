import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainFrom(QMainWindow):
    def __init__(self):
        super(MainFrom, self).__init__()

        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(200, 200, 700, 700)
        self.initUI()

    def initUI(self):
        self.lblSayi1 = QtWidgets.QLabel(self)
        self.lblSayi1.setText("Sayı1: ")
        self.lblSayi1.move(20, 20)

        self.txt_Sayi1 = QtWidgets.QLineEdit(self)
        self.txt_Sayi1.move(60, 20)
        self.txt_Sayi1.resize(150, 30)

        self.lblSayi2 = QtWidgets.QLabel(self)
        self.lblSayi2.setText("Sayı2: ")
        self.lblSayi2.move(20, 60)

        self.txt_Sayi2 = QtWidgets.QLineEdit(self)
        self.txt_Sayi2.move(60, 60)
        self.txt_Sayi2.resize(150, 30)

        self.buttonTopla = QtWidgets.QPushButton(self)
        self.buttonTopla.setText("Toplama")
        self.buttonTopla.move(60, 110)
        self.buttonTopla.clicked.connect(self.hesapla)

        self.buttonCikar = QtWidgets.QPushButton(self)
        self.buttonCikar.setText("Çıkarma")
        self.buttonCikar.move(60, 150)
        self.buttonCikar.clicked.connect(self.hesapla)

        self.buttonCarp = QtWidgets.QPushButton(self)
        self.buttonCarp.setText("Çarpma")
        self.buttonCarp.move(60, 190)
        self.buttonCarp.clicked.connect(self.hesapla)

        self.buttonBol = QtWidgets.QPushButton(self)
        self.buttonBol.setText("Bölme")
        self.buttonBol.move(60, 230)
        self.buttonBol.clicked.connect(self.hesapla)

        self.lbl_Sonuc = QtWidgets.QLabel(self)
        self.lbl_Sonuc.setText("SONUÇ : ")
        self.lbl_Sonuc.move(60, 270)

    def hesapla(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Toplama':
            result = int(self.txt_Sayi1.text()) + int(self.txt_Sayi2.text())
        elif sender == 'Çıkarma':
            result = int(self.txt_Sayi1.text()) - int(self.txt_Sayi2.text())
        elif sender == 'Çarpma':
            result = int(self.txt_Sayi1.text()) * int(self.txt_Sayi2.text())
        elif sender == 'Bölme':
            result = int(self.txt_Sayi1.text()) / int(self.txt_Sayi2.text())

        self.lbl_Sonuc.setText("SONUÇ : " + str(result))


def app():
    app = QApplication(sys.argv)
    win = MainFrom()

    win.show()
    sys.exit(app.exec_())


app()
