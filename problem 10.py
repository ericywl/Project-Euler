def prime(n):
    mult = set()
    for i in range(2, n+1):
        if i not in mult:
            yield i
            mult.update(range(i*i, n+1, i))
 
plist = list(prime(2 * 10**6))
print(sum(plist))

# using sieve of eratosthenes to generate a list of prime numbers and find the 10001st prime