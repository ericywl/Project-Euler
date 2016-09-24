col = set()
L = []

def collatz(i):
	x = 1
	num = i
	while i != 1:
		if i % 2 == 0:
			i = i // 2
			x += 1
			col.add(i)
		else:
			i = 3*i + 1
			x += 1
			col.add(i)
	L.append([x, num])

for n in range(10**6, 1, -1):
	if n not in col:
		col.add(n)
		collatz(n)

print(max(L))

# find number less than 1 million with the longest collatz chain
