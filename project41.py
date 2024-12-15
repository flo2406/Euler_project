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

def get_all_permutations_rec(n, actual_res):
    if len(actual_res) == n:
        return { int(actual_res) }

    res = set()
    for i in range(1, n + 1):
        if str(i) in actual_res:
            continue
        new_res = actual_res + str(i)
        res = res | get_all_permutations_rec(n, new_res)
    return res

def get_all_permutations(n):
    return get_all_permutations_rec(n, "")


def pandigital_prime():
    for i in range(9, 1, -1):
        perm = get_all_permutations(i)
        for val in sorted(perm, reverse=True):
            if is_prime(val):
                return val

    return 0

print(pandigital_prime())


