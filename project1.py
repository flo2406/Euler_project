#First soluce

def find_3_5_multiple_v1(n):
	res = 0
	for i in range(n):
		if i % 3 == 0:
			res += i
		elif i % 5 == 0:
			res += i
	return res

res = find_3_5_multiple_v1(1000)
print(res)



#Second soluce

# We can use the fact that the sum of multiple of y in the n first number is 
# y * sum of the first (n / y) numbers

# Moreover the n first number is equal to n * (n + 1) / 2

def find_3_5_multiple_v2(n):
	n = n - 1 # To not take care of 1000
	sum_multiple_3 = 3 * ((n // 3) * (n // 3 + 1)) // 2
	sum_multiple_5 = 5 * ((n // 5) * (n // 5 + 1)) // 2
	sum_multiple_15 = 15 * ((n // 15) * (n // 15 + 1)) // 2
	return sum_multiple_3 + sum_multiple_5 - sum_multiple_15

res = find_3_5_multiple_v2(1000)
print(res)