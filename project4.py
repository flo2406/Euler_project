# First soluce

def is_palindrome(n):
	arr = []
	while n >= 10:
		arr.append(n % 10)
		n  = n // 10
	arr.append(n)
	
	for i in range(len(arr) // 2 + 1):
		if (arr[i] != arr[-i - 1]):
			return False
	return True


def largest_palindrome_product():
	res = 0
	for i in range(1000,0,-1):
		for j in range(1000,0,-1):
			if (i * j > res and is_palindrome(i * j)):
				res = i * j
	return res

res = largest_palindrome_product()
print(res)