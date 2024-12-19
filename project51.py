def is_prime(n):
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        if i == 2:
            i += 1
        else:
            i += 2
    return True

def is_n_prime_value_family(val, n):
    not_prime = 0
    for i in range(10):
        if i == 0 and val[0] == '*':
            not_prime += 1
            continue
        nb = val.replace("*", str(i + int('0')))
        if not is_prime(int(nb)):
            not_prime += 1
            if not_prime > (10 - n):
                return False
    return True

# We can assume than the last digit cannot be wilcard (because if end by 0 / 2 or 4 is not prime)
# Need also at least 1 wildcard

def get_prime_digit_family_rec(str_val, size, n):
    len_str_val = len(str_val)
    if len_str_val == size:
        if '*' not in str_val:
            return None
        if is_n_prime_value_family(str_val, n):
            return str_val
        return None
    
    digits = [ '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    if size == 1:
        digits = [ '1', '3', '7', '9' ]
    elif len_str_val == 0:
        digits = [ '*', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

    for digit in digits:
        val = get_prime_digit_family_rec(str_val + digit, size, n)
        if val != None:
            return val


def get_prime_digit_family(n):
    for i in range(2, 10):
        val = get_prime_digit_family_rec('', i, n)
        if val != None:
            return val

print(get_prime_digit_family(8))