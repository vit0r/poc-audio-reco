# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\vnaraujo\projects\speechRecognition\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 360, 601, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLogger = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelLogger.setEnabled(False)
        self.labelLogger.setText("")
        self.labelLogger.setObjectName("labelLogger")
        self.horizontalLayout_2.addWidget(self.labelLogger)
        self.hsRuidoMin = QtWidgets.QSlider(self.centralwidget)
        self.hsRuidoMin.setEnabled(False)
        self.hsRuidoMin.setGeometry(QtCore.QRect(630, 370, 151, 22))
        self.hsRuidoMin.setOrientation(QtCore.Qt.Horizontal)
        self.hsRuidoMin.setObjectName("hsRuidoMin")
        self.hsRuidoMax = QtWidgets.QSlider(self.centralwidget)
        self.hsRuidoMax.setEnabled(False)
        self.hsRuidoMax.setGeometry(QtCore.QRect(630, 430, 151, 22))
        self.hsRuidoMax.setOrientation(QtCore.Qt.Horizontal)
        self.hsRuidoMax.setObjectName("hsRuidoMax")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 350, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 410, 71, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ruido minimo:"))
        self.label_2.setText(_translate("MainWindow", "Ruido máximo:"))
