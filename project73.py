import math

def count_frac_range(n, min_lim, max_lim):
    res = 0
    for num in range(1, n + 1):
        for den in range(num + 1, n + 1):
            if math.gcd(num, den) == 1 and num / den > min_lim and num / den < max_lim:
                res += 1
    
    return res

print(count_frac_range(12000, 1 / 3, 1 / 2))