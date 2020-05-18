import math
from lab7.entity.differential import Differential


class ThirdDiff(Differential):

    def f(self, x, y):
        return math.sin(x) * y