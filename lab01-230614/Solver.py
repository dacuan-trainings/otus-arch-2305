# Класс для решения квадратных уравнений
import gr_globals as grg
import math


class Solver:

    def print(self):
        print("Hello world!")
        return
    def sqrSolve(self, a, b, c):
        d = b**2 - 4*a*c
        res = [];
        if d < -grg.double_eps:
            # D < 0
            return []
        elif d < 0:
            # D == 0
            d = abs(d)
        sd = math.sqrt(d)
        res.append((-b - sd)/(2*a))
        res.append((-b + sd)/(2*a))
        return res