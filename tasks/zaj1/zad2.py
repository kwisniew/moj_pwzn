def range_1(x0,xN,n):
	lista = list(range(n));
	dx = (xN-x0)/n	
	#lista[0] = x0
	#lista[n-1] = xN
	for i in lista:
		lista[i]=x0+lista[i]*dx
	print (lista)

range_1(5,10,10)
	
