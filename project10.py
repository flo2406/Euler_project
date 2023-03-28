# First soluce

def erathostene(n):
	era = [ False ] * (n + 1)
	era[1] = True
	i = 2
	while (i * i <= n):
		if (not era[i]):
			j = 2 * i
			while (j <= n):
				era[j] = True
				j += i
		i += 1
	return era


def sum_prime(n):
	era = erathostene(n)
	res = 0
	for i in range(n + 1):
		if (not era[i]):
			res += i
	return res

res = sum_prime(2000000)
print(res)