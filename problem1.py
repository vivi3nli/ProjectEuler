#my simple solution without thinking

def Multi(below):
	count = 0
	for i in range(below):
		if i % 3 == 0 or i % 5 == 0:
			count += i
	return count

print "the sum of all 3 and 5 below 10 is ", Multi(10)
print "the sum of all 3 and 5 below 1000 is ", Multi(1000)

#below are solution from https://projecteuler.net/thread=1;page=5

# Optimal Solution to the best of my knowledge
def gauss_sum(n):	 # Find sum of all values between 0 and n
   return (n*(n+1))/2

def nsum(n, limit): # Find all sum of multiples of n between 0 and limit
   z = limit/n
   if limit%n == 0:
      z-=1
   return n*gauss_sum(z)

def mnsum(m, n, ceiling):
   # Multiples of mn occur twice (once for m, once for n) 
   # we subtract one of each such multiple
   return nsum(m, ceiling) + nsum(n, ceiling) - nsum(m*n, ceiling)

#or a really simple way
print sum(set(range(3,1000,3)) | set(range(5,1000,5)))

