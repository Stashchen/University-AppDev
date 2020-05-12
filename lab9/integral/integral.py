import numpy as np
from abc import abstractmethod
from pyqtgraph import PlotCurveItem, BarGraphItem


class Integral:

    def __init__(self, a, b, step):
        self.a = float(a)
        self.b = float(b)
        self.step = float(step)
        self.area = 0

        self.drawables = {}

    @abstractmethod
    def f(self, x):
        pass

    def count_main_integral(self):
        x = [val for val in np.arange(self.a, self.b + self.step, self.step)]
        y = [self.f(x_val) for x_val in x]

        self.drawables['main'] = PlotCurveItem(x=x, y=y, pen={'width': 3, 'color': 'b'})

    def count_left_rect(self):
        x = [val for val in np.arange(self.a, self.b + self.step, self.step)]
        y = [self.f(x_val) for x_val in x]

        for index, value in enumerate(x[1:]):
            self.area = y[index] * (value - x[index-1])

        self.drawables['bar'] = BarGraphItem(x=[x_val-(self.step/2) for x_val in x], height=y, width=self.step, brush='y', pen={'width': 3, 'color': 'r'})
        return 'left_rect'

    def count_right_rect(self):
        x = [val for val in np.arange(self.a, self.b + self.step, self.step)]
        y = [self.f(x_val) for x_val in x]

        for index, value in enumerate(x[1:]):
            self.area = y[index] * (value - x[index-1])

        self.drawables['bar'] = BarGraphItem(x=[x_val + (self.step / 2) for x_val in x], height=y, width=self.step,
                                             brush='y', pen={'width': 3, 'color': 'r'})
        return 'right_rect'

    def count_mid_rect(self):
        x = [val for val in np.arange(self.a, self.b + self.step, self.step)]
        y = [self.f(x_val) for x_val in x]

        for index, value in enumerate(x[1:]):
            self.area = y[index] * (value - x[index-1])

        self.drawables['bar'] = BarGraphItem(x=x, height=y, width=self.step, brush='y', pen={'width': 3, 'color': 'r'})
        return 'mid_rect'

    def count_trap(self):
        x = [val for val in np.arange(self.a, self.b + self.step, self.step)]
        y = [self.f(x_val) for x_val in x]

        for index, value in enumerate(x):
            self.area = (y[index] + y[index-1])/2 * (value - x[index-1])

        self.drawables['bar'] = PlotCurveItem(x=x, y=y, brush='y', fillBrush='y', fillLevel=1, pen={'width': 3, 'color': 'r'})
        return 'trap'

    def draw(self, window):
        for key in self.drawables:
            window.addItem(self.drawables[key])
