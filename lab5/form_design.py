# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blueprint.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1177, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(300, 20, 861, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 121))
        self.groupBox.setObjectName("groupBox")
        self.half_division_rb = QtWidgets.QRadioButton(self.groupBox)
        self.half_division_rb.setGeometry(QtCore.QRect(10, 30, 112, 23))
        self.half_division_rb.setChecked(True)
        self.half_division_rb.setObjectName("half_division_rb")
        self.iterations_rb = QtWidgets.QRadioButton(self.groupBox)
        self.iterations_rb.setGeometry(QtCore.QRect(10, 60, 112, 23))
        self.iterations_rb.setObjectName("iterations_rb")
        self.newton_rb = QtWidgets.QRadioButton(self.groupBox)
        self.newton_rb.setGeometry(QtCore.QRect(10, 90, 112, 23))
        self.newton_rb.setObjectName("newton_rb")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 271, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 251, 95))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.a_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.a_edit.setObjectName("a_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.a_edit)
        self.b_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.b_edit.setObjectName("b_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.b_edit)
        self.accuracy_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.accuracy_edit.setObjectName("accuracy_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.accuracy_edit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 280, 271, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.func_1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.func_1.setGeometry(QtCore.QRect(10, 30, 171, 23))
        self.func_1.setChecked(True)
        self.func_1.setObjectName("func_1")
        self.func_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.func_2.setGeometry(QtCore.QRect(10, 60, 171, 23))
        self.func_2.setObjectName("func_2")
        self.func_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.func_3.setGeometry(QtCore.QRect(10, 90, 181, 23))
        self.func_3.setObjectName("func_3")
        self.result_btn = QtWidgets.QPushButton(self.centralwidget)
        self.result_btn.setGeometry(QtCore.QRect(10, 410, 271, 81))
        self.result_btn.setObjectName("result_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(100, 510, 89, 25))
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 500, 861, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.result_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.result_edit.setReadOnly(True)
        self.result_edit.setObjectName("result_edit")
        self.horizontalLayout.addWidget(self.result_edit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 22))
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
        self.groupBox.setTitle(_translate("MainWindow", "Methods"))
        self.half_division_rb.setText(_translate("MainWindow", "half division"))
        self.iterations_rb.setText(_translate("MainWindow", "iterations"))
        self.newton_rb.setText(_translate("MainWindow", "Newton"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parametrs"))
        self.a_edit.setText(_translate("MainWindow", "-2"))
        self.b_edit.setText(_translate("MainWindow", "3"))
        self.accuracy_edit.setText(_translate("MainWindow", "0.001"))
        self.label.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "End"))
        self.label_3.setText(_translate("MainWindow", "Accuracy"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Equations"))
        self.func_1.setText(_translate("MainWindow", "x^2 + 2x - 3 = 0"))
        self.func_2.setText(_translate("MainWindow", "0.5*x^2 - 1 = 0"))
        self.func_3.setText(_translate("MainWindow", "0.25*x^3 + x - 1.25 = 0"))
        self.result_btn.setText(_translate("MainWindow", "Result"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "X = "))
from pyqtgraph import PlotWidget