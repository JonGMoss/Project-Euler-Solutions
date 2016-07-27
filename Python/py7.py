def isItaPrime(a):
	#Look for factors of 2 first
	if a == 1:
		return False
	elif a == 2:
		return True
	elif a == 3:
		return True	
	elif a%2==0:
		return False
	x = 3
	while x < a**0.5+1:
		if a%x==0:
			return False
		x += 2
	return True


def primeCounter(a):
	i = 1
	primelist = []
	while (len(primelist) < a):
		if isItaPrime(i):
			primelist.append(i)
			i=i+1
		else:
			i=i+1
	print primelist[a-1]

primeCounter(10001)
##104743
