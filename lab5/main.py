import sys
import form_design

from PyQt5 import QtWidgets
from entity import first_func as first, second_func as second, third_func as third


class MainApp(QtWidgets.QMainWindow, form_design.Ui_MainWindow):
    """docstring for MainApp"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # setting up design
        self.graphicsView.setBackground('w')
        self.graphicsView.showGrid(x=True, y=True)

        self.exit_btn.clicked.connect(sys.exit)
        self.result_btn.clicked.connect(self.draw)

    def draw(self):
        self.graphicsView.clear()

        if self.func_1.isChecked():
            equation = first.FirstFunction(float(self.a_edit.displayText()),
                                           float(self.b_edit.displayText()),
                                           float(self.accuracy_edit.displayText())
                                           )
        elif self.func_2.isChecked():
            equation = second.SecondFunction(float(self.a_edit.displayText()),
                                             float(self.b_edit.displayText()),
                                             float(self.accuracy_edit.displayText())
                                             )
        else:
            equation = third.ThirdFunction(float(self.a_edit.displayText()),
                                           float(self.b_edit.displayText()),
                                           float(self.accuracy_edit.displayText())
                                           )

        equation.get_main_integral()

        if self.half_division_rb.isChecked():
            result = equation.count_half_division()
        elif self.iterations_rb.isChecked():
            result = equation.count_iterations()
        else:
            result = equation.count_Newton()

        self.result_edit.setText(str(result))

        equation.draw_all(self.graphicsView)




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса MainApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
