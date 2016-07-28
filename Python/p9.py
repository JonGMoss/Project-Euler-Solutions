def pythagorianTriplet(n):
	for a in xrange(1, n/2):
		for b in xrange(1, (n-a)/2,1):
			c = n-a-b
			if a**2+b**2==c**2:
				if a < b:
					print a*b*c

pythagorianTriplet(1000)

#31875000
