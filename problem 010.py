def prime(n):
	mult = set()
	for i in range(2, n+1):
		if i not in mult:
			yield i
			mult.update(range(i*i, n+1, i))

# use sieve of eratosthenes to generate primes
 
plist = list(prime(2 * 10**6))
print(sum(plist))

# find the sum of primes less than or equal to 2 million