import math

# Use this method that use diophantine approximation of square root to solve diophantine equations
# https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/HCMUNS7.pdf
# https://en.wikipedia.org/wiki/Pell%27s_equation

# Code from project 64

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

# End of code project 64

# Code similar from project 65

def sqrt_convergent(n, nb_iter):
    if n <= 0:
        return None

    repetitive_part = get_block_frac_sqrt(n)
    seq = repetitive_part.copy()
    while len(seq) < nb_iter:
        seq += repetitive_part

    seq = seq[:nb_iter - 1]

    seq_len = len(seq)
    first_nb = int(math.sqrt(n))

    num = 0
    den = 1

    if seq_len != 0:
        num = 1
        den = seq[-1]
        seq.pop()
        for e in seq[::-1]:
            next_num = den
            next_den = num + e * den
            num = next_num
            den = next_den
    
    num += first_nb * den
    return num, den

# End of code project 65


def is_square(n):
    sqrt_res = math.sqrt(n)
    return sqrt_res == int(sqrt_res)

def minimal_x_diophantine_eq(D):
    if is_square(D):
        return None
    
    nb_iter = 1
    while True:
        num, den = sqrt_convergent(D, nb_iter)

        if num * num - D * den * den == 1:
            return num

        nb_iter += 1

    """ First version not opti
    y = 1
    while True:
        x_2 = (D * y ** 2 + 1)
        if is_square(x_2):
            return int(math.sqrt(x_2)), y
        y += 1
    """

def diophatine_equation(limit):
    val_max = 0
    res = 0

    for i in range(1, limit + 1):
        dio_eq_res = minimal_x_diophantine_eq(i)
        if dio_eq_res is not None and dio_eq_res > val_max:
            res = i
            val_max = dio_eq_res
    return res

print(diophatine_equation(1000))