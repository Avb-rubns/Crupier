# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saldoJ = QtWidgets.QLabel(self.centralwidget)
        self.saldoJ.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saldoJ.setFont(font)
        self.saldoJ.setObjectName("saldoJ")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.play.setObjectName("play")
        self.saldoC = QtWidgets.QLabel(self.centralwidget)
        self.saldoC.setGeometry(QtCore.QRect(410, 10, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saldoC.setFont(font)
        self.saldoC.setObjectName("saldoC")
        self.label_apostar = QtWidgets.QLabel(self.centralwidget)
        self.label_apostar.setGeometry(QtCore.QRect(10, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_apostar.setFont(font)
        self.label_apostar.setObjectName("label_apostar")
        self.label_numero = QtWidgets.QLabel(self.centralwidget)
        self.label_numero.setGeometry(QtCore.QRect(10, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_numero.setFont(font)
        self.label_numero.setObjectName("label_numero")
        self.input_apuesta = QtWidgets.QLineEdit(self.centralwidget)
        self.input_apuesta.setGeometry(QtCore.QRect(220, 60, 71, 20))
        self.input_apuesta.setObjectName("input_apuesta")
        self.input_num = QtWidgets.QSpinBox(self.centralwidget)
        self.input_num.setGeometry(QtCore.QRect(130, 100, 42, 22))
        self.input_num.setObjectName("input_num")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(510, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num.setFont(font)
        self.num.setObjectName("num")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(520, 210, 75, 23))
        self.reset.setObjectName("reset")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(280, 110, 101, 81))
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.msg = QtWidgets.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(220, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setText("")
        self.msg.setObjectName("msg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 21))
        self.menubar.setObjectName("menubar")
        self.menuinfo = QtWidgets.QMenu(self.menubar)
        self.menuinfo.setObjectName("menuinfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuinfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saldoJ.setText(_translate("MainWindow", "Su saldo:"))
        self.play.setText(_translate("MainWindow", "Jugar"))
        self.saldoC.setText(_translate("MainWindow", "Saldo Crupier:"))
        self.label_apostar.setText(_translate("MainWindow", "Ingrese una cantidad a postar:"))
        self.label_numero.setText(_translate("MainWindow", "Eliga un numero:"))
        self.label.setText(_translate("MainWindow", "Numero que salio:"))
        self.num.setText(_translate("MainWindow", "0"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.menuinfo.setTitle(_translate("MainWindow", "info"))
