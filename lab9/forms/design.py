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
        MainWindow.resize(1155, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.draw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.draw_btn.setGeometry(QtCore.QRect(780, 500, 221, 51))
        self.draw_btn.setObjectName("draw_btn")
        self.paintingView = PlotWidget(self.centralwidget)
        self.paintingView.setGeometry(QtCore.QRect(610, 10, 531, 471))
        self.paintingView.setObjectName("paintingView")
        self.reset_drawing_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_drawing_btn.setGeometry(QtCore.QRect(830, 560, 111, 41))
        self.reset_drawing_btn.setObjectName("reset_drawing_btn")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 581, 421))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 440, 581, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.n_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.n_edit.setObjectName("n_edit")
        self.gridLayout.addWidget(self.n_edit, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.a_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.a_edit.setObjectName("a_edit")
        self.gridLayout.addWidget(self.a_edit, 0, 1, 1, 1)
        self.b_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.b_edit.setObjectName("b_edit")
        self.gridLayout.addWidget(self.b_edit, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.method_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.method_label.setObjectName("method_label")
        self.gridLayout.addWidget(self.method_label, 1, 1, 1, 1)
        self.func_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.func_label.setObjectName("func_label")
        self.gridLayout.addWidget(self.func_label, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        self.graph_btn = QtWidgets.QPushButton(self.centralwidget)
        self.graph_btn.setGeometry(QtCore.QRect(80, 550, 221, 51))
        self.graph_btn.setObjectName("graph_btn")
        self.reset_graph_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_graph_btn.setGeometry(QtCore.QRect(340, 550, 111, 51))
        self.reset_graph_btn.setObjectName("reset_graph_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1155, 22))
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
        self.draw_btn.setText(_translate("MainWindow", "Start/Stop"))
        self.reset_drawing_btn.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "a = "))
        self.label_2.setText(_translate("MainWindow", "b ="))
        self.label_3.setText(_translate("MainWindow", "step ="))
        self.label_4.setText(_translate("MainWindow", "Method:"))
        self.label_5.setText(_translate("MainWindow", "Function:"))
        self.method_label.setText(_translate("MainWindow", "method_1"))
        self.func_label.setText(_translate("MainWindow", "func_1"))
        self.label_6.setText(_translate("MainWindow", "Result = "))
        self.graph_btn.setText(_translate("MainWindow", "Start/Stop"))
        self.reset_graph_btn.setText(_translate("MainWindow", "Reset"))
from pyqtgraph import PlotWidget