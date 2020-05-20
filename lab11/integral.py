import numpy as np
import pyqtgraph as pq


class Integral:

    def __init__(self, a, b, step):
        self.a = float(a)
        self.b = float(b)
        self.step = float(step)

        self.area = 0

        self.drawables = {}

    def f(self, x):
        return np.sin(x) / np.sqrt(x)

    def get_main_integral(self):
        self.x = [val for val in np.arange(self.b, self.a + self.step, self.step)]
        self.y = [self.f(x_val) for x_val in self.x]

        self.drawables['main'] = pq.PlotCurveItem(x=self.x, y=self.y, pen={'width': 3,
                                                                           'color': 'b'})

    def count_left(self):
        area = 0
        x = [val - self.step / 2 for val in self.x]

        for index, val in enumerate(self.x[1:]):
            area += (val - x[index]) * self.y[index]

        self.area = area
        self.drawables['method'] = pq.BarGraphItem(x=x, height=self.y, width=self.step,
                                                   pen={'width': 2, 'color': 'r'},
                                                   brush='y'
                                                   )

    def count_right(self):
        area = 0
        x = [val + self.step / 2 for val in self.x]

        for index, val in enumerate(self.x[1:]):
            area += (val - x[index]) * self.y[index]

        self.area = area
        self.drawables['method'] = pq.BarGraphItem(x=x, height=self.y, width=self.step,
                                                   pen={'width': 2, 'color': 'r'},
                                                   brush='y'
                                                   )

    def count_mid(self):
        area = 0

        for index, val in enumerate(self.x[1:]):
            area += (val - self.x[index]) * self.y[index]

        self.area = area
        self.drawables['method'] = pq.BarGraphItem(x=self.x, height=self.y, width=self.step,
                                                   pen={'width': 2, 'color': 'r'},
                                                   brush='y'
                                                   )

    def count_trap(self):
        area = 0

        for index, val in enumerate(self.x[1:]):
            area += (val - self.x[index]) / 2 * self.y[index]

        self.area = area
        self.drawables['main'] = pq.PlotCurveItem(x=self.x,
                                                  y=self.y,
                                                  pen={'width': 3,
                                                       'color': 'b'},
                                                  fillLevel=0,
                                                  brush='y'
                                                  )

    def draw(self, window):
        try:
            window.addItem(self.drawables['method'])
            window.addItem(self.drawables['main'])
        except:
            window.addItem(self.drawables['main'])