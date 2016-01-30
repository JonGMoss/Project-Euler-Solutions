
def isitprime(a):
	"is it prime?"
	if a >= 2:
		for b in range(2,a):
			if not (a%b):
			 return False
	else:
		return False
	return True

def PrimeFactors(a):
	"Will find all prime factors of a number a"
	i = 2
	while (i < 600851475143**0.5):
			if a%i==0:
				if isitprime(i):
					print i
			i=i+1
	return;

print 'prime factors are:'
PrimeFactors(600851475143)
