l = list(range(10))
sum =0
def key(x):
	global sum
	sum=sum+1
	return x
sorted(l, key=key)
print(sum)

