# First soluce

def smallest_multiple_v1(n):
	res = 1
	while True:
		is_ok = True
		for i in range(1,n + 1):
			if res % i != 0:
				is_ok = False
				break
		if (is_ok):
			break
		res += 1
	return res

res = smallest_multiple_v1(10)
print(res)



# Second soluce

def erathostene(n):
	era = [ 1 ] * (n + 1)
	i = 2
	while (i * i <= n):
		if (era[i] == 1):
			j = 2 * i
			while (j <= n):
				era[j] = 0
				j += i
		i += 1
	return era

def decompose_and_add(nb, n, era):
	arr = [ 0 ] * n
	for i in range(2, n):
		while (nb % i == 0):
			arr[i] += 1
			nb = nb // i

	for i in range(2, n):
		era[i] = max(era[i], arr[i])

	return



def smallest_multiple_v2(n):
	res = 1
	era = erathostene(n)
	for i in range(2, n):
		decompose_and_add(i, n, era)

	for i in range(2,n):
		res *= pow(i, era[i])
	return res


res = smallest_multiple_v2(20)
print(res)