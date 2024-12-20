def reverse(val):
    return int(str(val)[::-1])

def is_palindrome(val):
    return str(val)[::-1] == str(val)

def is_lychrel_number(val, max_iter):
    for i in range(max_iter):
        new_val = val + reverse(val)
        if is_palindrome(new_val):
            return False
        val = new_val
    return True

def number_of_lychrel_number(limit, max_iter):
    res = 0
    for i in range(limit):
        if is_lychrel_number(i, max_iter):
            res += 1
    return res

print(number_of_lychrel_number(10000, 50))
