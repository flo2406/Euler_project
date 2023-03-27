import math

# First intuitive soluce

def is_prime(n):
	for i in range(2,n):
		if (n % i == 0):
			return False
	return True


def largest_prime_factor_v1(n):
	res = 1
	for i in range(2,n):
		if (is_prime(i) and n % i == 0):
			res = i
	return res


#res = largest_prime_factor_v1(13195)
#print(res)


# Second soluce

# The erathostene enable to have an array of true an false depending if the number is prime or not.
# It is possible to calcul it very quickly because, the loop can be stop after the square root of the number. 
# After it is juste necessary to know if the number is prime and if the number is a multiple of the number.

# Default : Need a lot of memory to save array


def erathostene(n):
	era = [ False ] * (n + 1)
	i = 2
	while (i * i <= n):
		if (not era[i]):
			j = 2 * i
			while (j <= n):
				era[j] = True
				j += i
		i += 1
	return era

def largest_prime_factor_v2(n):
	era = erathostene(n // 2)
	i = 2
	res = 1
	while (i * i <= n):
		if (not era[i] and n % i == 0):
			if (not era[n // i] and n // i > res):
				return n // i
			if (i > res):
				res = i
		i += 1
	return res


#res = largest_prime_factor_v2(13195)
#print(res)



# Third soluce

# The goal is to divide at each time by the multiple which are obviously prime because if the facto is not prime, it was divide before.
# And it is possible to stop after the square root.

def largest_prime_factor_v3(n):
	res = 1
	while (n % 2 == 0):
		n = n // 2
		res = 2

	facto = 3
	while (n > 1 and facto * facto <= n):
		while (n % facto == 0):
			n = n // facto
			res = facto
		facto += 2

	if (n != 1):
		res = n

	return res

res = largest_prime_factor_v3(600851475143)
print(res)