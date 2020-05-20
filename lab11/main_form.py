import sys
from pyqtgraph import PlotWidget
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from forms.design import Ui_MainWindow
from integral import Integral


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start_btn.clicked.connect(self.show_new)

    def show_new(self):
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setBackground('w')
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
        self.right_rb.setChecked(True)
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
        self.step_edit.setText('0.1')
        self.b_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.b_edit.setGeometry(QtCore.QRect(50, 261, 173, 25))
        self.b_edit.setObjectName("b_edit")
        self.b_edit.setText('1')
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
        self.a_edit.setText('2')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(7, 488, 47, 89))
        self.label.setObjectName("label")
        self.result_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.result_edit.setGeometry(QtCore.QRect(60, 520, 726, 25))
        self.result_edit.setReadOnly(True)
        self.result_edit.setObjectName("result_edit")

        _translate = QtCore.QCoreApplication.translate
        self.draw_btn.setText(_translate("MainWindow", "Draw"))
        self.label.setText(_translate("MainWindow", "Result:"))
        self.groupBox.setTitle(_translate("MainWindow", "Method"))
        self.right_rb.setText(_translate("MainWindow", "Right rect"))
        self.left_rb.setText(_translate("MainWindow", "Left rect"))
        self.mid_rb.setText(_translate("MainWindow", "Mid rect"))
        self.trap_rb.setText(_translate("MainWindow", "Trapezi"))
        self.label_2.setText(_translate("MainWindow", "sin(x)/sqrt(x)"))
        self.label_3.setText(_translate("MainWindow", "a"))
        self.label_4.setText(_translate("MainWindow", "b"))
        self.label_5.setText(_translate("MainWindow", "step"))

        self.graphicsView.show()
        self.draw_btn.show()
        self.label.show()
        self.groupBox.show()
        self.right_rb.show()
        self.left_rb.show()
        self.mid_rb.show()
        self.trap_rb.show()
        self.label_2.show()
        self.result_edit.show()
        self.a_edit.show()
        self.b_edit.show()
        self.step_edit.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()

        self.draw_btn.clicked.connect(self.build_integral)

    def build_integral(self):
        self.graphicsView.clear()
        integral = Integral(self.a_edit.text(),
                            self.b_edit.text(),
                            self.step_edit.text()
                            )

        integral.get_main_integral()

        if self.left_rb.isChecked():
            integral.count_left()
        elif self.right_rb.isChecked():
            integral.count_right()
        elif self.mid_rb.isChecked():
            integral.count_mid()
        else:
            integral.count_trap()

        self.result_edit.setText(str(integral.area))

        integral.draw(self.graphicsView)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    app.exec_()