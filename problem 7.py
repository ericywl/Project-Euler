def prime(n):
    mult = set()
    for i in range(2, n+1):
        if i not in mult:
            yield i
            mult.update(range(i*i, n+1, i))
 
plist = list(prime(1000000))
print(plist[10000])

# using sieve of eratosthenes to generate a list of prime numbers and find the 10001st prime