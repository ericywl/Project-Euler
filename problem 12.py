flist = set()

import math
import functools

def factors(n):    
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
	if len(factors(n)) > 500:
		print(n)

# find first triangle number with more than 500 factors







