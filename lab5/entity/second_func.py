from entity.equation import Equation


class SecondFunction(Equation):

    def f(self, x):
        return 0.5 * x**2 - 1

    def df(self, x):
        return x

    def get_x_from_equation(self, x):
        return x + 0.5 * x**2 - 1

    def g(self, x):
        return 1 + x
