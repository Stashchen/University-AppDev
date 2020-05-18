import numpy as num
import pyqtgraph as pq


class Integral:
    """ Integral base class """

    def __init__(self, a, b, step):
        self.a = a
        self.b = b
        self.step = step
        self.__x = []
        self.__y = []
        self.__integral_item = None

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, value):
        self.__step = value

    def count_area_trapeze(self):
        area = 0
        for index in range(1, len(self.__x)):
            area += (self.__y[index - 1] + self.__y[index]) * (self.__x[index] + self.__x[index - 1]) / 2
        return area

    def count_area_right_rect(self):
        area = 0
        for index in range(1, len(self.__x)):
            area += (self.__x[index] + self.__x[index - 1]) * self.__y[index]
        return area

    def count_area_left_rect(self):
        area = 0
        for index in range(1, len(self.__x)):
            area += (self.__x[index] + self.__x[index - 1]) * self.__y[index - 1]
        return area

    def count_area_mid_rect(self):
        area = 0
        for index in range(1, len(self.__x)):
            area += (self.__x[index] + self.__x[index - 1]) * (self.__y[index] + self.__y[index - 1]) / 2
        return area

    def count_formula(self, x):
        return num.sin(x) / num.sqrt(x)

    def count_integral_points(self):
        self.__x = [round(val, 4) for val in num.arange(self.a, self.b+self.__step, self.step)]
        for x in self.__x:
            self.__y.append(self.count_formula(x))

    def create_integral_item(self, pen_width, pen_color, fill_color, fill_width=0, bar=False):
        if bar:
            self.__integral_item = pq.BarGraphItem(x=self.__x,
                                                   y1=self.__y,
                                                   width=self.__step,
                                                   pen={'width': pen_width,
                                                        'color': pen_color},
                                                   brush=fill_color)
        else:
            self.__integral_item = pq.PlotCurveItem(x=self.__x,
                                                    y=self.__y,
                                                    pen={'width': pen_width,
                                                         'color': pen_color},
                                                    fillLevel=fill_width,
                                                    brush=fill_color)

    def draw(self, window):
        window.addItem(self.__integral_item)

    def remove(self, window):
        window.removeItem(self.__integral_item)
