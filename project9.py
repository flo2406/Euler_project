import math

# First soluce

def special_pyta_triplet():
	for a in range(500):
		for b in range(a + 1, 500):
			c_2 = a * a + b * b
			c = math.sqrt(c_2)
			if (math.floor(c) == c and a + b + c == 1000):
				return a * b * int(c)


res = special_pyta_triplet()
print(res)
