class Integrator(object):  
	def __init__(self): 
		self.stop ={
			3:(1 ,4 ,1 ,         1/3  ),
			4:(1 ,3 ,3 ,1 ,      3/8  ),
			5:(7 ,32,12,32,7 ,   2/45 ),
			6:(19,75,50,50,75,19,5/288),
		}
			

	def integrate(self, xo, xn, n, fun, stp):
		x=xo
		val=0
		h = (xn-xo)/n/(stp-1)
		for i in range(n):
			for j, el in enumerate(self.stop[stp][0:-1]):
				if j==(len(self.stop[stp])-2):
					val+=el*fun(x)*h*self.stop[stp][-1]
				else:			
					val+=el*fun(x)*h*self.stop[stp][-1]
					x+=h
		return val

def fun(x):
    return x*x

x=Integrator()
print((x.integrate(0,2,10000,fun,6)))
