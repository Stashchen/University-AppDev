import math
from lab9.integral.integral import Integral


class FuncTwo(Integral):

    def __str__(self):
        return 'ln(1+x^2)/(1+x^2)'

    def f(self, x):
        return math.log10(1 + x**2)/(1 + x**2)