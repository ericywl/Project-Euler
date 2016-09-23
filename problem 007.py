def prime(n):
	mult = set()
	for i in range(2, n+1):
		if i not in mult:
			yield i
			mult.update(range(i*i, n+1, i))

# use sieve of eratosthenes to generate primes
 
plist = list(prime(1000000))
print(plist[10000])

# find the 10001st prime