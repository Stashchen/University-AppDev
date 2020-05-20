from abc import abstractmethod
from pyqtgraph import ScatterPlotItem, PlotCurveItem
import numpy as np


class Differential:

    def __init__(self, a, b, step):
        self.a = a
        self.b = b
        self.step = step
        
        self.x_lst = []
        self.y_lst = []

        self._drawables = {}

    @property
    def x_lst(self):
        return self._x_lst

    @x_lst.setter
    def x_lst(self, value):
        self._x_lst = value

    @property
    def y_lst(self):
        return self._y_lst

    @y_lst.setter
    def y_lst(self, value):
        self._y_lst = value

    @abstractmethod
    def f(self, x, y):
        pass

    def reset_x_y(self):
        self.x_lst = [x for x in np.arange(self.a, self.b + self.step, self.step)]
        self.y_lst = [1]
    
    def count_Euler(self):
        for x in self.x_lst[1:]:
            next_y = self.y_lst[-1] + self.step * self.f(x, self.y_lst[-1])
            self.y_lst.append(next_y)

        self._drawables['second_lines'] = PlotCurveItem(x=self.x_lst, y=self.y_lst, pen={'width': 2, 'color': 'b'})
        self._drawables['second_dots'] = ScatterPlotItem(x=self.x_lst, y=self.y_lst, pen={'width': 3, 'color': 'r'})

    def count_ext_Euler(self):
        for x in self.x_lst[1:]:
            y = self.y_lst[-1]

            k1 = self.step * self.f(x, y)
            k2 = self.step * self.f(x + self.step, y + k1)

            next_y = self.y_lst[-1] + .5 * (k1 + k2)
            self.y_lst.append(next_y)

        self._drawables['second_lines'] = PlotCurveItem(x=self.x_lst, y=self.y_lst, pen={'width': 2, 'color': 'b'})
        self._drawables['second_dots'] = ScatterPlotItem(x=self.x_lst, y=self.y_lst, pen={'width': 3, 'color': 'r'})

    def count_runge_kut_third(self):
        for x in self.x_lst[1:]:
            y = self.y_lst[-1]

            k1 = self.step * self.f(x, y)
            k2 = self.step * self.f(x + .5 * self.step, y + .5 * k1)
            k3 = self.step * self.f(x + self.step, y + 2 * k2 + k1)

            next_y = self.y_lst[-1] + 1 / 6 * (k1 + 4 * k2 + k3)
            self.y_lst.append(next_y)

        self._drawables['second_lines'] = PlotCurveItem(x=self.x_lst, y=self.y_lst, pen={'width': 2, 'color': 'b'})
        self._drawables['second_dots'] = ScatterPlotItem(x=self.x_lst, y=self.y_lst, pen={'width': 3, 'color': 'r'})

    def count_runge_kut_forth(self):
        for x in self.x_lst[1:]:
            y = self.y_lst[-1]

            k1 = self.step * self.f(x, y)
            k2 = self.step * self.f(x + .5 * self.step, y + .5 * k1)
            k3 = self.step * self.f(x + .5 * self.step, y + .5 * k2)
            k4 = self.step * self.f(x + self.step, y + k3)

            next_y = self.y_lst[-1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

            self.y_lst.append(next_y)

        self._drawables['second_lines'] = PlotCurveItem(x=self.x_lst, y=self.y_lst, pen={'width': 2, 'color': 'b'})
        self._drawables['second_dots'] = ScatterPlotItem(x=self.x_lst, y=self.y_lst, pen={'width': 3, 'color': 'r'})

    def draw(self, window):
        for key in self._drawables:
            window.addItem(self._drawables[key])
