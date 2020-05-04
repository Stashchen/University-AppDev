from entity.equation import Equation


class ThirdFunction(Equation):

    def f(self, x):
        return 0.25 * x**3 + x - 1.25

    def df(self, x):
        return 0.25 * 3 * x**2 + 1

    def get_x_from_equation(self, x):
        return 1.25 / (0.25 * x**2 + 1)

    def g(self, x):
        return (-10 * x)/(x**2 + 4)**2
