import math

# Need to make operation on fractions and not on float
def get_next_rest(n, num, den, a):
    den_int = (n - den ** 2) / num
    num_update = - den - (den_int * a)
    next_num = int(den_int)
    next_den = int(num_update)
    return next_num, next_den

def get_block_frac_sqrt(n):
    real_sqrt = math.sqrt(n)
    first = int(real_sqrt)
    rest_num = 1
    rest_den = - first
    
    if rest_den + real_sqrt == 0:
        return None
    
    rest = rest_num / (real_sqrt + rest_den)
    a = int(rest)

    res = []
    rest_list = []
    while True:
        if rest_den + real_sqrt == 0:
            return None
        if rest in rest_list:
            return res
        res.append(a)
        rest_list.append(rest)

        rest_num, rest_den = get_next_rest(n, rest_num, rest_den, a) 
        rest = rest_num / (real_sqrt + rest_den)
        a = int(rest)

def odd_period_square_root(limit):
    res = 0
    for i in range(limit + 1):
        block_frac = get_block_frac_sqrt(i)
        if block_frac is not None and len(block_frac) % 2 == 1:
            res += 1
    return res

print(odd_period_square_root(10000))