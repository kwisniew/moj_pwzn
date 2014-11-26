import math

def furier(furier_arg, points, fun):
    T=5
    values = []
    x=0
    for i in points:
        for j, jj in enumerate(furier_arg):
            if j==0:
                x=jj/2
            else:
                if fun == 'sin':
                    x+=jj*math.sin(2*j*math.pi*i/T)
                if fun == 'cos':
                    x+=jj*math.cos(2*j*math.pi*i/T)
        values.append(x)
    return(values)
    
points = [0, 0.7, 1.4, 2.1, 2.8]
furier_arg = [1,2,3,4,5]
print(furier(furier_arg, points, 'sin'))