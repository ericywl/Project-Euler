import math
import functools
from itertools import chain, cycle, accumulate

def factors1(n):    
    return set(functools.reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

trisum = 1
x = 2
trilist = set()

while trisum < 10**8:
	trisum += x
	x += 1
	trilist.add(trisum)

# triangle numbers generator

for n in trilist:
	if len(factors1(n)) > 500:
		print(n)

# find first triangle number with more than 500 factors

def factors2(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))
 
    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r

# more efficient code for factors






