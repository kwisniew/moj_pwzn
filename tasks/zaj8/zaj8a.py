import time


import pyximport; pyximport.install()
import zaj8 

import numpy as np

a=time.monotonic()
zaj8.quicksort(np.random.rand(1000000), 0, (1000000-1))
b=time.monotonic()

print(b-a)
