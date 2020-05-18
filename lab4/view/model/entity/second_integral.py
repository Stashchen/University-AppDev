import numpy as num
from .integral import Integral


class SecondIntegral(Integral):

    def count_formula(self, x):
        return num.cos(num.pi * x / 6) / num.sqrt(x)
