import sys
import controller.blueprint as blueprint
import random as r
from model.entity.integral import Integral
from model.entity.second_integral import SecondIntegral
from model.entity.third_integral import ThirdIntegral
from PyQt5 import QtWidgets


def check_valid_line_edit(line_edit):
    try:
        value = float(line_edit.text())
        return value
    except ValueError:
        return 0


class MainApp(QtWidgets.QMainWindow, blueprint.Ui_MainWindow):
    """docstring for MainApp"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # setting up design
        self.graphicsView.setBackground('w')

        # binding buttons
        self.pushButton_2.clicked.connect(self.show_integral)


        self.integral_1 = Integral(float(self.low_1.text()),
                                   float(self.high_1.text()),
                                   float(self.step_1.text())
                                   )
        self.integral_2 = Integral(float(self.low_2.text()),
                                   float(self.high_2.text()),
                                   float(self.step_2.text())
                                   )

        self.show_integral()

    def show_integral(self):
        self.integral_1.remove(self.graphicsView)

        a = check_valid_line_edit(self.low_1)
        b = check_valid_line_edit(self.high_1)
        step = check_valid_line_edit(self.step_1)

        if self.first_function_1.isChecked():
            new_integral = Integral(a, b, step)
        elif self.second_function_1.isChecked():
            new_integral = SecondIntegral(a, b, step)
        else:
            new_integral = ThirdIntegral(a, b, step)

        new_integral.count_integral_points()

        if self.trapeze_1.isChecked():
            area = new_integral.count_area_trapeze()
        elif self.left_1.isChecked():
            area = new_integral.count_area_left_rect()
        elif self.right_1.isChecked():
            area = new_integral.count_area_right_rect()
        else:
            area = new_integral.count_area_mid_rect()

        self.lineEdit_7.setText(str(area))

        new_integral.create_integral_item(3,
                                          r.choice(['r', 'g', 'b']),
                                          (r.randint(0, 250), r.randint(0, 250), r.randint(0, 250), 200))

        new_integral.draw(self.graphicsView)
        self.integral_1 = new_integral

        self.integral_2.remove(self.graphicsView)

        a = check_valid_line_edit(self.low_2)
        b = check_valid_line_edit(self.high_2)
        step = check_valid_line_edit(self.step_2)

        if self.first_function_2.isChecked():
            new_integral = Integral(a, b, step)
        elif self.second_function_2.isChecked():
            new_integral = SecondIntegral(a, b, step)
        else:
            new_integral = ThirdIntegral(a, b, step)

        new_integral.count_integral_points()

        if self.trapeze_2.isChecked():
            area = new_integral.count_area_trapeze()
        elif self.left_2.isChecked():
            area = new_integral.count_area_left_rect()
        elif self.right_2.isChecked():
            area = new_integral.count_area_right_rect()
        else:
            area = new_integral.count_area_mid_rect()

        self.lineEdit_8.setText(str(area))
        self.lineEdit_9.setText(str(check_valid_line_edit(self.lineEdit_7) + check_valid_line_edit(self.lineEdit_8)))
        self.lineEdit_10.setText(str(check_valid_line_edit(self.lineEdit_7) - check_valid_line_edit(self.lineEdit_8)))

        new_integral.create_integral_item(3,
                                          r.choice(['r', 'g', 'b']),
                                          (r.randint(0, 250), r.randint(0, 250), r.randint(0, 250), 150))

        new_integral.draw(self.graphicsView)
        self.integral_2 = new_integral


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса MainApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
