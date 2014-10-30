# -*- coding: utf-8 -*-

import math


class Integrator(object):

    @classmethod
    def get_level_parameters(cls, level):
       
        param = [[1/2, 1/2],[1/3, 4/3, 1/3],[3/8, 9/8, 9/8, 3/8],[14/45, 64/45, 24/45, 64/45, 14/45]]
        return param[level]

    def __init__(self, level):

        self.level = level

    def integrate(self, func, func_range, num_evaluations):
        value = 0
        h = (func_range[1]-func_range[0])/(num_evaluations//self.level)
        dx = h / (self.level-1)
        param = self.get_level_parameters(self.level-2)       
        for x in range(num_evaluations//self.level):
            for y in range(self.level):
                value += func(y*dx + x*h + func_range[0])*param[y]*dx
        return value



if __name__ == '__main__':
    i = Integrator(3)
    print(i.integrate(math.sin, (0, 2*math.pi), 30))
    print(i.integrate(lambda x: x*x, (0, 1), 30))
