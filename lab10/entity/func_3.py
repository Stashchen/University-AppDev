import math
from entity.differential import Differential


class ThirdDiff(Differential):

    def f(self, x, y):
        return math.sin(x) * y