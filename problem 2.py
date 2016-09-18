x = 1
y = 2
add = 0

fib = [1, 2]

while x + y <= 4 * 10**6:
	z = x + y
	x, y = y, z
	fib.append(z)

for i in fib:
	if i % 2 == 0:
		add = add + i
	else:
		continue

print(add)

# sum of all even fibonacci numbers <= 4 million