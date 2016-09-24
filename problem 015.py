from math import factorial

def path(m, n):
    numerator = factorial(m + n)
    denominator = factorial(m) * factorial(n)
    print(numerator//denominator)

path(20, 20)

# find the number of routes through a 20x20 grid (only down and right)