import math
import random
from lab9.integral.integral import Integral


class FuncThree(Integral):

    def __str__(self):
        return 'sin(x)/sqrt(x)'

    def f(self, x):
        return math.sin(x)/math.sqrt(x)