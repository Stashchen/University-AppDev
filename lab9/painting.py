from pyqtgraph import ScatterPlotItem


class Painting:

    def __init__(self):
        self.x = []
        self.y = []
        self.pen = {'width': 10, 'color': 'r'}
        self.item = ScatterPlotItem(self.x, self.y, self.pen)

    def draw(self, window):
        window.currentItem = self.item
