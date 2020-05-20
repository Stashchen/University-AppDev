# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_widgets.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 20, 561, 451))
        self.graphicsView.setObjectName("graphicsView")
        self.draw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.draw_btn.setGeometry(QtCore.QRect(10, 340, 211, 131))
        self.draw_btn.setObjectName("draw_btn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 211, 151))
        self.groupBox.setObjectName("groupBox")
        self.right_rb = QtWidgets.QRadioButton(self.groupBox)
        self.right_rb.setGeometry(QtCore.QRect(10, 30, 112, 23))
        self.right_rb.setObjectName("right_rb")
        self.left_rb = QtWidgets.QRadioButton(self.groupBox)
        self.left_rb.setGeometry(QtCore.QRect(10, 60, 112, 23))
        self.left_rb.setObjectName("left_rb")
        self.mid_rb = QtWidgets.QRadioButton(self.groupBox)
        self.mid_rb.setGeometry(QtCore.QRect(10, 90, 112, 23))
        self.mid_rb.setObjectName("mid_rb")
        self.trap_rb = QtWidgets.QRadioButton(self.groupBox)
        self.trap_rb.setGeometry(QtCore.QRect(10, 120, 112, 23))
        self.trap_rb.setObjectName("trap_rb")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 121, 17))
        self.label_2.setObjectName("label_2")
        self.step_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.step_edit.setGeometry(QtCore.QRect(50, 292, 173, 25))
        self.step_edit.setObjectName("step_edit")
        self.b_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.b_edit.setGeometry(QtCore.QRect(50, 261, 173, 25))
        self.b_edit.setObjectName("b_edit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(14, 261, 9, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(14, 292, 30, 25))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(14, 230, 8, 25))
        self.label_3.setObjectName("label_3")
        self.a_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.a_edit.setGeometry(QtCore.QRect(50, 230, 173, 25))
        self.a_edit.setObjectName("a_edit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(7, 488, 47, 89))
        self.label.setObjectName("label")
        self.result_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.result_edit.setGeometry(QtCore.QRect(60, 520, 726, 25))
        self.result_edit.setReadOnly(True)
        self.result_edit.setObjectName("result_edit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.draw_btn.setText(_translate("MainWindow", "Draw"))
        self.groupBox.setTitle(_translate("MainWindow", "Method"))
        self.right_rb.setText(_translate("MainWindow", "Right rect"))
        self.left_rb.setText(_translate("MainWindow", "Left rect"))
        self.mid_rb.setText(_translate("MainWindow", "Mid rect"))
        self.trap_rb.setText(_translate("MainWindow", "Trapezi"))
        self.label_2.setText(_translate("MainWindow", "sin(x)/sqrt(x)"))
        self.label_4.setText(_translate("MainWindow", "b"))
        self.label_5.setText(_translate("MainWindow", "step"))
        self.label_3.setText(_translate("MainWindow", "a"))
        self.label.setText(_translate("MainWindow", "Result:"))
