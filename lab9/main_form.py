import time
import numpy as np
import random

from PyQt5.QtWidgets import QMainWindow
from lab9.forms.design import Ui_MainWindow
from pyqtgraph import ScatterPlotItem
from PyQt5.QtCore import QTimer
from lab9.integral.func_1 import FuncOne
from lab9.integral.func_2 import FuncTwo
from lab9.integral.func_3 import FuncThree


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start_painting_flag = False
        self.start_graph_flag = False

        self.paintingView.currentItem = ScatterPlotItem(x=[], y=[], pen={'width': 10, 'color': 'r'})
        self.paintingView.addItem(self.paintingView.currentItem)

        self.graph_btn.clicked.connect(self.start_graph)
        self.reset_graph_btn.clicked.connect(self.graphicsView.clear)

        self.draw_btn.clicked.connect(self.start_stop_painting)
        self.reset_drawing_btn.clicked.connect(self.reset_painting)

    def reset_painting(self):
        self.paintingView.removeItem(self.paintingView.currentItem)
        self.start_painting_flag = False

        self.paintingView.currentItem = ScatterPlotItem(x=[], y=[], pen={'width': 10, 'color': 'r'})
        self.paintingView.addItem(self.paintingView.currentItem)

    def start_stop_painting(self):
        if self.start_painting_flag:
            self.start_painting_flag = False
        else:
            self.start_painting_flag = True

        self.start_painting()

    def start_painting(self):
        a = random.randint(1, 8)
        b = random.randint(1, 15)
        c = random.randint(3, 15)
        f = np.pi / 10
        x = int(np.sin(c * f) * np.cos(a * f) * 150) + 150
        y = int(np.sin(c * f) * np.sin(b * f) * 150) + 150
        self.paintingView.currentItem.addPoints(x=[x], y=[y])
        if self.start_painting_flag:
            QTimer.singleShot(1, self.start_painting)

    def start_graph(self):
        if self.start_graph_flag:
            self.start_graph_flag = False
        else:
            self.start_graph_flag = True

        self.build_graph()

    def build_graph(self):
        self.graphicsView.clear()
        tmp = random.choice([FuncOne, FuncTwo, FuncThree])
        a = random.randint(1, 10)
        b = random.randint(a + 5, a + 10)
        step = random.random()

        function = tmp(a, b, step)
        method = random.choice([function.count_left_rect,
                              function.count_right_rect,
                              function.count_mid_rect,
                              function.count_trap
                              ])
        method_name = method()
        function.count_main_integral()

        self.func_label.setText(str(function))
        self.method_label.setText(method_name)
        self.a_edit.setText(str(a))
        self.b_edit.setText(str(b))
        self.n_edit.setText('{:.2f}'.format(step))
        self.lineEdit.setText('{:.4f}'.format(function.area))

        function.draw(self.graphicsView)
        time.sleep(.3)

        if self.start_graph_flag:
            QTimer.singleShot(1, self.build_graph)
