import math

# Square equations solver
class Solver:

    #empty constructor
    def __init__(self):
        pass

    def sqrSolve(self, a, b, c):
        d = b**2 - 4*a*c
        res = [];
        if d < 0:
            # D < 0
            return res
        
        sd = math.sqrt(d)
        res.append((-b - sd)/(2*a))
        res.append((-b + sd)/(2*a))
        return res
