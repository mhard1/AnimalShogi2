# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'C:\Users\sofmap\AnimalShogi\main_window.ui'
# Created by: PyQt5 UI code generator 5.13.0
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 687)
        MainWindow.setStyleSheet("background:rgb(255, 255, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 991, 531))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 550, 251, 101))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("font: 75 36pt \"Comic Sans MS\"; color: white; background:rgb(255, 170, 100)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 550, 251, 101))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("font: 75 36pt \"Comic Sans MS\"; color: white; background:rgb(255, 170, 100)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 550, 251, 101))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("font: 75 36pt \"Comic Sans MS\"; color: white; background:rgb(255, 170, 100)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.clicked.connect(self.quitbtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animal Shogi"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/animal_shogi_main.jpg\"/></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "New Game"))
        self.pushButton_5.setText(_translate("MainWindow", "Rules"))
        self.pushButton_6.setText(_translate("MainWindow", "Quit"))

    def quitbtn(self):
        if self.pushButton_6.isChecked():
            sys.exit()

import main_image_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
