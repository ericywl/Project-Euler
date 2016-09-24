def pytri(n=1000):
	for z in range(5, n+1):
		sq_z = z * z
		sq_x = x = 1
		y = z - 1
		sq_y = y * y
		while x < y:
			if sq_x + sq_y == sq_z:
				yield x, y, z
				x += 1; sq_x = x * x
				y -= 1; sq_y = y * y
			elif sq_x + sq_y < sq_z:
				x += 1; sq_x = x * x
			else:
				y -= 1; sq_y = y * y

for a, b, c in list(pytri(1000)):
	if a + b + c == 1000:
		print(a*b*c)

# find the product of the pythagorean triplet that has a sum of 1000