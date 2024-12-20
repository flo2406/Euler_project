# Next value of num and den recursivly 
#
# 1 + 1 / (1 + num / den)
# 1 + 1 / ((num + den) / den) 
# 1 + den / (num + den)
# (den + num + den) / (num + den)
# num = 2 * den + num   and  den = num + den


# We can test with the first example :
# N1: num = 3 / den = 2
# N2: num = 2 * 2 + 3 = 7 / den = 2 + 3 = 5
# N3: num = 2 * 5 + 7 = 17 / den = 5 + 7 = 12

def square_root_2_converg_frac(limit):
    res = 0
    num = 2
    den = 3
    for _ in range(1, limit):
        tmp_num = num
        num = 2 * den + num
        den = tmp_num + den
        if len(str(num)) > len(str(den)):
            res += 1
    return res

print(square_root_2_converg_frac(1000))