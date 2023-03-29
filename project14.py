import numpy as np

# First soluce

def apply_collatz_v1(i):
	if (i == 1):
		return 0

	elif (i % 2 == 0):
		return 1 + apply_collatz_v1(i // 2)

	return 1 + apply_collatz_v1(3 * i + 1)


def find_max_line_collatz_v1(n):
	res = 0
	res_line = 0
	for i in range(1,n):
		line = apply_collatz_v1(i)
		if (line > res_line):
			res_line = line
			res = i

	return res


#res = find_max_line_collatz_v1(1000000)
#print(res)


# Second soluce

def apply_collatz_v2(i, tab):
	if (i >= len(tab)):
		if (i % 2 == 0):
			return 1 + apply_collatz_v2(i // 2, tab)
		return 1 + apply_collatz_v2(3 * i + 1, tab)

	if (tab[i] != -1):
		return tab[i]

	elif (i % 2 == 0):
		res = 1 + apply_collatz_v2(i // 2, tab)
		tab[i] = res
		return res

	res = 1 + apply_collatz_v2(3 * i + 1, tab)
	tab[i] = res
	return res

def find_max_line_collatz_v2(n):
	tab = [ -1 ] * n
	tab[1] = 0
	for i in range(1,n):
		apply_collatz_v2(i, tab)

	return np.argmax(tab)


res = find_max_line_collatz_v2(1000000)
print(res)
