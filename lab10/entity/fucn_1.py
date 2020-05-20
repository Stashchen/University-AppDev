from entity.differential import Differential


class FirstDiff(Differential):

    def f(self, x, y):
        return 3*x - 2*y + 5