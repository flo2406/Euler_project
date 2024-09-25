# First soluce

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

def get_nb_quad_prime(a, b):
    n = 0
    res = 0
    while True:
        val = n * n + a * n + b
        if not is_prime(val):
            return res
        res += 1
        n += 1

def most_quad_prime():
    max_quad = 0
    res = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            val = get_nb_quad_prime(a, b)
            if val > max_quad:
                max_quad = val
                res = a * b
    return res

print(most_quad_prime())