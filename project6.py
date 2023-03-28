# First soluce

def sum_square(n):
	res = 0
	for i in range(n + 1):
		res += i * i
	return res

def square_sum(n):
	res = 0
	for i in range(n + 1):
		res += i
	return res * res

def sum_square_diff_v1(n):
	return square_sum(n) - sum_square(n)


res = sum_square_diff_v1(100)
print(res)



# Second soluce

def sum_square_diff_v2(n):
	sum_square = n * (n + 1) * (2 * n + 1) // 6
	square_sum = (n * (n + 1) // 2) * (n * (n + 1) // 2)
	return square_sum - sum_square

res = sum_square_diff_v2(100)
print(res)
