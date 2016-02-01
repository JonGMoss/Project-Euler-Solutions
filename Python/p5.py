#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def GetConsecutiveRemainders(a):
	x=1
	for x in xrange(2520,2147483647,2520):
	#can be sped up further by increasing the step size to.
	#step size of 2520 is picked as it must be a factor of the correct value
		for i in range(1,a+1):
			if x%i==0:
				if i == a:
					print 'success',x
					return
			else:
				break
		x=x+1
	else:
		print 'No consectutive remainders up to',a,'in',x

GetConsecutiveRemainders(20)
