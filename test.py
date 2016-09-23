import functools
import operator
import math

def function(n):
    j = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            j += [i, n//i]
    return j
