from entity.differential import Differential


class SecondDiff(Differential):

    def f(self, x, y):
        return x**2 - y