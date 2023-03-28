# First soluce

def count_all_factor(n):
	res = 0
	facto = 1
	while (facto * facto < n):
		if (n % facto == 0):
			res += 2
		facto += 1
	if (facto * facto == n):
		res += 1
	return res


def triangular_number_factor(n):
	i = 1
	sum_ = 1
	while True:
		if (count_all_factor(sum_) >= n):
			return sum_
		i += 1
		sum_ += i


res = triangular_number_factor(500)
print(res)