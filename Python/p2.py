def fibbonacci_print_evens(n):
	"prints all fibbonacci numbers divisible by 2 up to a value of n"
	a = 0
 	b = 1
	for i in range(n-1):
		a,b = b,a+b
		if a%2==0:
			print a
	return;


print fibbonacci_print_all(34)