# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_tableFrom.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 281, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(380, 10, 113, 20))
        self.txtName.setObjectName("txtName")
        self.txtPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrice.setGeometry(QtCore.QRect(380, 50, 113, 20))
        self.txtPrice.setObjectName("txtPrice")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(380, 100, 75, 23))
        self.btnSave.setObjectName("btnSave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))
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
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
