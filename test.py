i = [1, 2, 3, 4, 5, 6]

import functools
import operator

p = functools.reduce(operator.mul, i[0:4])
print(p)