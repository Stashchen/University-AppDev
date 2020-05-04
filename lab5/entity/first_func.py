from entity.equation import Equation


class FirstFunction(Equation):

    def f(self, x):
        return x**2 + 2*x - 3

    def df(self, x):
        return 2*x + 2

    def get_x_from_equation(self, x):
        return 3 / (x + 2)

    def g(self, x):
        return -3/(x + 2)**2
