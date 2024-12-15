import math

def pow_mod(a, x, n):
    mod = 10 ** n
    res = 1
    while x > 0:
        if x % 2 == 1:
            res = (res * a) % mod
        a = (a * a) % mod
        x >>= 1
    return res

def sum_self_power(n):
    res = 0
    for i in range(1, n + 1):
        res += pow_mod(i, i, 10)
    return res % 10 ** 10
    
print(sum_self_power(1000))