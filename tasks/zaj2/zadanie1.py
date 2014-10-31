# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
    lista =[]
    if step==None:
        step=1
    if stop==None:
        tmp        = start_stop
        start_stop = 0
        stop       = tmp
    while(start_stop < stop):
        yield start_stop
        start_stop +=step
    
y = list(xrange(5))
x=list(range(5))
print(x)
print(y)