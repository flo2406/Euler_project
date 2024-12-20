def sum_digit(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n //10
    return res

def powerful_digit_sum(max_a, max_b):
    res = 0
    for a in range(max_a):
        for b in range(max_b):
            res = max(res, sum_digit(a ** b))
    return res

print(powerful_digit_sum(100, 100))