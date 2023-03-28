# First soluce

def is_prime(n):
	if (n % 2 == 0):
		return False

	i = 3
	while (i * i <= n):
		if (n % i == 0):
			return False
		i += 2
	return True


def prime_n(n):
	if (n == 1):
		return 2
	i = 3
	m = 1
	while (m != n):
		if (is_prime(i)):
			m += 1
		i += 2
	return i - 2


res = prime_n(10001)
print(res)