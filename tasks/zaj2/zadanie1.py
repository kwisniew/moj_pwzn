# -*- coding: utf-8 -*-
def xrange(start_stop, stop=None, step=None):
	i=0
	stop2=start_stop
	if stop==None:		
		start_stop=0
		stop=stop2		
	if step==None:
		step=1
	while(i<((stop-start_stop)/step)):
		yield (start_stop+i*step)
		i+=1
xrange(-3,10,2)

#    """
#    Funkcja która działa jak funkcja range (wbudowana i z poprzednich #zajęć)
#    która działa dla liczb całkowitych.
#    """
