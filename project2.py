#First intuitive soluce

def sum_even_fibo_v1(limit):
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


res = sum_even_fibo_v1(4000000)
print(res)


#Second soluce

# We can see that the second number (2) and every 3 number are even
# Moreover, we can prove that F(n) = 4 * F(n - 3) + F(n - 6) and we can compute only even number

# F(n) = F(n - 1) + F(n - 2)
# F(n) = F(n - 2) + F(n - 3) + F(n - 2)
# F(n) = F(n - 3) + F(n - 4) + F(n - 3) + F(n - 3) + F(n - 4)
# F(n) = 3 * F(n - 3) + 2 * F(n - 4)
# F(n) = 3 * F(n - 3) + F(n - 4) + F(n - 5) + F(n - 6)
# F(n) = 4 * F(n - 3) + F(n - 6)


def sum_even_fibo_v2(limit):
	tmp1 = 0
	tmp2 = 2
	res = 0
	while (tmp2 < limit):
		res += tmp2
		tmp = tmp1
		tmp1 = tmp2
		tmp2 = 4 * tmp1 + tmp
	return res


res = sum_even_fibo_v2(4000000)
print(res)
