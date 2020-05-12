import math
from lab9.integral.integral import Integral


class FuncOne(Integral):

    def __str__(self):
        return 'cos(pi*x/6)/sqrt(x)'

    def f(self, x):
        return math.cos(math.pi * x / 6) / math.sqrt(x)
