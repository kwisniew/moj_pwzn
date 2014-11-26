class Integrator(object):  
    def __init__(self, xo, xn, n, fun): 
        self.xo = xo
        self.xn = xn
        self.n  = n
        self.dx = (xn-xo)/n
        self.fun= fun
        self.val= 0

class RectangleIntegrator(Integrator): 
    def integrate(self):
        dxx=self.xo
        for i in range(self.n):
            self.val+=fun(dxx+self.dx/2)*self.dx
            dxx+=self.dx
        return self.val

class TrapezoidIntegrator(Integrator):
    def integrate(self):
        dxx=self.xo
        for i in range(self.n):
            self.val+=(fun(dxx)+fun(dxx+self.dx))/2*self.dx
            dxx+=self.dx
            
        return self.val
    
class SimpsonIntegrator(Integrator):
    def integrate(self):
        dxx=self.xo
        for i in range(self.n):
            self.val+=(fun(dxx)+4*fun(dxx+self.dx/2)+fun(dxx+self.dx))/6*self.dx
            dxx+=self.dx
        return self.val
    
def fun(x):
    return x*x


Rec=RectangleIntegrator(0,2,1000,fun)
x=Rec.integrate()
print ('%.3f' % x)
Tra=TrapezoidIntegrator(0,2,1000,fun)
x=Tra.integrate()
print ('%.3f' % x)
Sim=SimpsonIntegrator(0,2,1000,fun)
x=Sim.integrate()
print ('%.3f' % x)
