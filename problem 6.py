summ = 0
add = 0
square = 0

for a in range(1, 101):
	summ +=  a ** 2

# find sum of squares of natural numbers 1-100

for b in range(1, 101):
	add += b
	square = add ** 2

# find square of sum of natural numbers 1-100

print(square - summ)

# print the difference between the two