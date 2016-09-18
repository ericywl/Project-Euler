num1 = 13195
num2 = 600851475143

i = 2

#solution 1

while num2 > i ** 2:
	while num2 % i == 0:
		num2 = num2 // i
	i = i + 1

print(num2)

#solution 2

while num2 != 1:
    if num2 % i == 0:
    	num2 /= i
    else:
    	i += 1
    	
print(i)

# largest prime factor in a given number




