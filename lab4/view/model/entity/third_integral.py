import numpy as num
from .integral import Integral


class ThirdIntegral(Integral):

    def count_formula(self, x):
        return 1 / (1 + num.sin(x) ** 3)
