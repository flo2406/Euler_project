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

def get_all_rotation(n):
    rotation = { n }
    n_str = str(n)
    nb_digit = len(str(n))
    for _ in range(nb_digit - 1):
        n_str = n_str[1:] + n_str[0]
        rotation.add(int(n_str))
    return rotation

# Can avoid all number than contain even digit in it (can divide by 2)
# Can avoid all number than contain 5 in it (can divide by 5)

# Idea : Test all combinaisons with 1, 3, 7 and 7 with 2 -> 6 digits (limit to 1 million)
def combinaison(size):
    possible_number = [1, 3, 7, 9]

    if size == 1:
        res = set()
        for i in possible_number:
            res.add(i)
        return res
    
    last_res = combinaison(size - 1)
    res = set()
    for last_val in last_res:
        for i in possible_number:
            res.add(last_val * 10 + i)
    return res


def get_all_circular_prime():
    res = {2, 3, 5, 7}
    for nb_digit in range(2, 7):
        for comb in combinaison(nb_digit):
            if comb in res:
                continue
            rotation = get_all_rotation(comb)
            all_prime = True
            for r in rotation:
                if not is_prime(r):
                    all_prime = False
                    break
            if all_prime:
                res = res | rotation
    return res

print(len(get_all_circular_prime()))