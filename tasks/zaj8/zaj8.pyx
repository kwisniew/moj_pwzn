import numpy as np
cimport numpy as np

import cython
cimport cython
import timeit

cpdef unsigned int partition(np.ndarray[np.float64_t, ndim=1] list, int start, int end):
	cpdef float pivot = list[end]				# Partition around the last value
	cpdef int bottom = start-1		  		# Start outside the area to be partitioned
	cpdef int top = end			 		# Ditto

	cpdef int done = 0
	while not done:						# Until all elements are partitioned...

		while not done:					# Until we find an out of place element...
			bottom = bottom+1			# ... move the bottom up.

			if bottom == top:			# If we hit the top...
				done = 1			# ... we are done.
				break

			if list[bottom] > pivot:		# Is the bottom out of place?
				list[top] = list[bottom]	# Then put it at the top...
				break				# ... and start searching from the top.

		while not done:					# Until we find an out of place element...
			top = top-1				# ... move the top down.

			if top == bottom:			# If we hit the bottom...
				done = 1			# ... we are done.
				break

			if list[top] < pivot:			# Is the top out of place?
				list[bottom] = list[top]	# Then put it at the bottom...
				break				# ...and start searching from the bottom.

	list[top] = pivot					# Put the pivot in its place.
	return top						# Return the split point

@cython.boundscheck(False)
cpdef int quicksort(np.ndarray[np.float64_t, ndim=1] list, int start, int end):
	cpdef int split
	if start < end:						# If there are two or more elements...
		split = partition(list, start, end)		# ... partition the sublist...
		quicksort(list, start, split-1)			# ... and sort both halves.
		quicksort(list, split+1, end)
	return 0

