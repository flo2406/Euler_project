def sum_even_fibo(limit):
	tmp1 = 1
	tmp2 = 2
	res = 2
	while (tmp2 < limit):
		tmp = tmp1
		tmp1 = tmp2
		tmp2 = tmp + tmp1
		if (tmp2 % 2 == 0):
			res += tmp2
	return res


res = sum_even_fibo(4000000)
print(res)