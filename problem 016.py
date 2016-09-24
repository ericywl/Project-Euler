def power_digit_sum(n):
	num = 2**n
	summ = 0
	for i in str(num):
		summ += int(i)
	print(summ)

power_digit_sum(1000)

# find the sum of the digits of the number 2^n
