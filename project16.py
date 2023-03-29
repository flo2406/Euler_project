# First soluce

def sum_number(n):
	res = 0
	while n >= 10:
		res += n % 10
		n = n // 10
	res += n
	return res

res = sum_number(2 ** 1000)
print(res)