def facto(n):
    res = 1
    while n > 1:
        res *= n
        n = n - 1
    return res

def combinatoric(n, r):
    num = facto(n)
    den = facto(r) * facto(n - r)

    return num / den

def combinatoric_selection(limit):
    res = 0
    for n in range(1, limit + 1):
        for r in range(0, n + 1):
            val = combinatoric(n, r)
            if val > 1000000:
                res += 1
    return res

print(combinatoric_selection(100))
