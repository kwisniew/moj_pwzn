# -*- coding: utf-8 -*-

import math


class Integrator(object):

    @classmethod
    def get_level_parameters(cls, level):
       
        param = [[1/2, 1/2],[1/3, 4/3, 1/3],[3/8, 9/8, 9/8, 3/8],[14/45, 64/45, 24/45, 64/45, 14/45],[95/288, 375/288, 250/288, 250/288, 375/288, 95/288],[41/140, 216/140, 27/140, 272/140, 27/140, 216/140, 41/140],[(7*751)/17280, (7*3577)/17280, (7*1323)/17280, (7*2989)/17280,(7*2989)/17280, (7*1323)/17280, (7*3577)/17280, (7*751)/17280 ],[(4*989)/14175, (4*5888)/14175, -(4*928)/14175 ,(4*10496)/14175,-(4*4540)/14175, (4*10496)/14175, -(4*928)/14175, (4*5888)/14175,(4*989)/14175],[(9*2857)/89600, (9*15741)/89600, (9*1080)/89600, (9*19344)/89600,
(9*5778)/89600, (9*5778)/89600, (9*19344)/89600, (9*1080)/89600(9*15741)/89600, (9*2857)/89600],[(5*16067)/299376, (5*106300)/299376, -(5*48525)/299376,(5*272400)/299376, -(5*260550)/299376, (5*427368)/299376,-(5*260550)/299376, (5*272400)/299376, -(5*48525)/299376,(5*106300)/299376, (5*16067)/299376]]
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
