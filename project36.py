def is_palindrome(str):
	for i in range(len(str) // 2 + 1):
		if (str[i] != str[-i - 1]):
			return False
	return True

def get_str_bin(n):
	return str(bin(n))[2:]

def sum_double_base_palindromes(limit):
    res = 0
    for i in range(limit):
        str_dec = str(i)
        if not is_palindrome(str_dec):
            continue
        if not is_palindrome(get_str_bin(i)):
            continue
        res += i
    return res

print(sum_double_base_palindromes(1000000))
