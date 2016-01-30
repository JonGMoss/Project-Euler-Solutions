def SumOfMultiplesOfAandBinX(a,b,x):
	"Find the sum of two multiples a and b for a number x"
	c = 0
	for i in range(0, x):
		if i%a==0 or i%b==0:
			c=c+i
	print c
	return;

SumOfMultiplesOfAandBinX(3,5,1000)
