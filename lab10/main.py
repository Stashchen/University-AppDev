import sys

import PyQt5.QtWidgets as QtWidgets
from forms.design import Ui_MainWindow

from entity.fucn_1 import FirstDiff
from entity.func_2 import SecondDiff
from entity.func_3 import ThirdDiff


class MainMenu(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.graphicsView.setBackground('w')
        self.graphicsView.showGrid(x=True, y=True)

        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.graphicsView.clear()
        self.all_equations = []

        if self.func_1.isChecked():
            self.equation = FirstDiff(float(self.start_edit.text()),
                                      float(self.end_edit.text()),
                                      float(self.accuracy_edit.text())
                                      )
        elif self.func_2.isChecked():
            self.equation = SecondDiff(float(self.start_edit.text()),
                                       float(self.end_edit.text()),
                                       float(self.accuracy_edit.text())
                                       )
        else:
            self.equation = ThirdDiff(float(self.start_edit.text()),
                                      float(self.end_edit.text()),
                                      float(self.accuracy_edit.text())
                                      )

        if self.func_7.isChecked():
            self.equation_2 = FirstDiff(float(self.start_edit_3.text()),
                                        float(self.end_edit_3.text()),
                                        float(self.accuracy_edit_3.text())
                                        )
        elif self.func_8.isChecked():
            self.equation_2 = SecondDiff(float(self.start_edit_3.text()),
                                        float(self.end_edit_3.text()),
                                        float(self.accuracy_edit_3.text())
                                        )
        else:
            self.equation_2 = ThirdDiff(float(self.start_edit_3.text()),
                                        float(self.end_edit_3.text()),
                                        float(self.accuracy_edit_3.text())
                                        )

        if self.func_10.isChecked():
            self.equation_3 = FirstDiff(float(self.start_edit_4.text()),
                                        float(self.end_edit_4.text()),
                                        float(self.accuracy_edit_4.text())
                                        )
        elif self.func_11.isChecked():
            self.equation_3 = SecondDiff(float(self.start_edit_4.text()),
                                        float(self.end_edit_4.text()),
                                        float(self.accuracy_edit_4.text())
                                        )
        else:
            self.equation_3 = ThirdDiff(float(self.start_edit_4.text()),
                                        float(self.end_edit_4.text()),
                                        float(self.accuracy_edit_4.text())
                                        )

        self.all_equations.extend([self.equation, self.equation_2, self.equation_3])

        for equation in self.all_equations:
            equation.reset_x_y()

        if self.euler_method.isChecked():
            self.all_equations[0].count_Euler()
        elif self.ext_euler_method.isChecked():
            self.all_equations[0].count_ext_Euler()
        elif self.runge_kut_3_method.isChecked():
            self.all_equations[0].count_runge_kut_third()
        else:
            self.all_equations[0].count_runge_kut_forth()

        if self.euler_method_3.isChecked():
            self.all_equations[1].count_Euler()
        elif self.ext_euler_method_3.isChecked():
            self.all_equations[1].count_ext_Euler()
        elif self.runge_kut_3_method_3.isChecked():
            self.all_equations[1].count_runge_kut_third()
        else:
            self.all_equations[1].count_runge_kut_forth()

        if self.euler_method_4.isChecked():
            self.all_equations[2].count_Euler()
        elif self.ext_euler_method_4.isChecked():
            self.all_equations[2].count_ext_Euler()
        elif self.runge_kut_3_method_4.isChecked():
            self.all_equations[2].count_runge_kut_third()
        else:
            self.all_equations[2].count_runge_kut_forth()

        for equation in self.all_equations:
            equation.draw(self.graphicsView)

        for equation in self.all_equations:
            self.change_table(equation.x_lst, equation.y_lst, self.result_table)

    def change_table(self, x_lst, y_lst, table):

        table.setColumnCount(len(x_lst))
        table.setHorizontalHeaderLabels(["N_{}".format(index) for index in range(1, 1 + len(x_lst))])

        for index, val in enumerate(x_lst):
            table.setItem(0, index, QtWidgets.QTableWidgetItem('{:.2f}'.format(val)))
            table.setItem(1, index, QtWidgets.QTableWidgetItem('{:.4f}'.format(y_lst[index])))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainMenu()
    window.show()
    app.exec_()
