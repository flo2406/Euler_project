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

def get_diag_square():
    diag = [ 1 ]
    value = 1
    offset = 2

    nb_prime = 0
    nb_diag = 1
    while True:
        for _ in range(4):
            value += offset
            diag.append(value)
            nb_diag += 1
            if is_prime(value):
                nb_prime += 1
        offset += 2
        percent = nb_prime / nb_diag * 100
        if percent < 10:
            return ((nb_diag - 1) // 2) + 1

print(get_diag_square())

