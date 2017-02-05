#previous version
'''
def Sum():
	i = 1
	Sum = 0
	n = [1,2]
	for  n[i] in range(4000000):
		if n[i] % 2 == 0:
			Sum += n[i]
		n.append(n[i] + n[i - 1])
		i += 1

print Sum()
'''

#how about doing it recursively
'''
my version is rather slow because I have to generate the fib number 
recurisively first then to compare it to the standards
'''
def Sum_re(i):
    '''
    To get the No.i fibbonacci number recursively
    '''
    if i == 0 or i == 1:
        return 1
    return(Sum_re(i - 1) + Sum_re(i - 2))

def add_even(below):
    '''
    below, the largest fib number
    results, sum of all even numbers
    i, order of number
    '''
    result = 0
    i = 0
    while Sum_re(i) < below:
        if Sum_re(i) % 2 == 0:
            result += Sum_re(i)
        i += 1
    return result

#print(add_even(4000000))

#A really simple and quick one posted on https://projecteuler.net/thread=2
'''
This may be a small improvement.  The Fibonacci series is:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
Now, replacing an odd number with O and an even with E, we get:
O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...
And so each third number is even.  We don't need to calculate 
the odd numbers.  Starting from an two odd terms x, y, the series is:
x, y, x + y, x + 2y, 2x + 3y, 3x + 5y
And in Python, my solution is:
'''
def calcE():
	x = y = 1
	sum = 0
	while (sum < 4000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return sum
print(calcE())