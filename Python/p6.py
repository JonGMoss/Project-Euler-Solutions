def SumOfSquares(a):
    Sum = (a*(a+1)*(2*a+1))/6
    return Sum

def SquareOfSums(a):
    Square = a * (a+1) / 2
    return Square * Square

def DiffSumOfSquaresSquareOfSums(a):
    b = SquareOfSums(a)
    c = SumOfSquares(a)
    d = b-c
    print d

DiffSumOfSquaresSquareOfSums(100)
