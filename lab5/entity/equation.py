from abc import ABCMeta, abstractmethod

import numpy as num
from pyqtgraph import PlotCurveItem, ScatterPlotItem


class Equation:

    def __init__(self, a, b, step):
        self.a = a
        self.b = b
        self.step = step

        self.__drawables = {}

    @abstractmethod
    def f(self, x):
        pass

    @abstractmethod
    def df(self, x):
        pass

    @abstractmethod
    def get_x_from_equation(self, x):
        pass

    @abstractmethod
    def g(self, x):
        pass

    # Methods
    def get_main_integral(self):
        x = [val for val in num.arange(self.a, self.b, self.step)]
        y = [self.f(val) for val in num.arange(self.a, self.b, self.step)]

        self.__drawables['main'] = PlotCurveItem(x=x, y=y, pen={'width': 3, 'color': 'b'})

    def count_half_division(self):
        try:
            x_min, x_max = self.check_valid_values()
        except:
            return None

        avrg = (x_min + x_max)/2
        y = self.f(avrg)

        x_val = [avrg]

        while round(y, 2) != 0:
            avrg = (x_min + x_max)/2
            y = self.f(avrg)

            if y > 0:
                x_max = avrg
                x_val.append(x_max)

            elif y < 0:
                x_min = avrg
                x_val.append(x_min)

        self.__drawables['dots'] = ScatterPlotItem(x=x_val, y=[0 for _ in range(len(x_val))], pen={'width': 3, 'color': 'r'})
        try:
            del self.__drawables['method']
        except KeyError:
            pass

        return x_val[-1]

    def count_iterations(self):
        try:
            x, x1 = self.check_valid_values()
        except TypeError:
            return None

        x = (x + x1)/2

        x_next = self.get_x_from_equation(x)

        x_val = [x, x_next]
        y_val = [self.f(x) for x in x_val]

        while abs(x_next - x) > self.step:
            x = x_next
            if abs(self.g(x)) > 1:
                return None

            x_next = self.get_x_from_equation(x)

            x_val.append(x_next)
            y_val.append(self.f(x_next))

        self.__drawables['method'] = PlotCurveItem(x=x_val, y=y_val, pen={'width': 3, 'color': 'g'})
        self.__drawables['dots'] = ScatterPlotItem(x=x_val, y=y_val, pen={'width': 3, 'color': 'r'})

        return x_val[-1]


    def count_Newton(self):
        x_val = []
        y_val = []

        try:
            x = self.check_valid_values()[1]
        except:
            return None

        y = self.f(x)

        while round(y, len(str(self.step))-2):
            y = self.f(x)

            x_val.append(x)
            y_val.append(y)

            x = x - self.f(x)/self.df(x)

        self.__drawables['method'] = PlotCurveItem(x=x_val, y=y_val, pen={'width': 3, 'color': 'g'})
        self.__drawables['dots'] = ScatterPlotItem(x=x_val, y=y_val, pen={'width': 3, 'color': 'r'})

        return x_val[-1]

    def check_valid_values(self):
        if (self.f(self.a) * self.f(self.b)) > 0:
            return 0
        else:
            if self.a > 0:
                return (self.b, self.a)
            else:
                return (self.a, self.b)


    # Draw methods
    def draw_all(self, window):
        for item in self.__drawables:
            window.addItem(self.__drawables[item])

    def remove_all(self, window):
        for item in self.__drawables:
            window.removeItem(item)
