pal = []

for i in range(100 ** 2, 1000 ** 2):
	if str(i) == str(i)[::-1]:
		pal.append(i)

for n in pal:
	for x in range(100, 1000):
		if 99 < n / x < 1000 and n % x == 0:
			print(x, n//x, n)

# largest palindrome product of two 3-digit numbers
