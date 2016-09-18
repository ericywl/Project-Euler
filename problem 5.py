# 2 3 4 5 6 7 8 9 10
# 2 3 2 5 1 7 2 3 1

primes = []
powers = []
pro = 1

for y in range(2, 21):
	for z in range(2, y):
		if y % z == 0:
			break
	else:
		primes.append(y)

# prime number generator

for c in range(1, 5):
	for p in primes:
		powers.append(p ** c)

# powers of prime generator

for i in range(2, 21):
	for x in range(2, i):
		while i % x == 0 and i not in primes:
			if i not in powers:
				i = 1
			else:
				i = i // x
	else:
		pro = pro * i

print(pro)

# 

