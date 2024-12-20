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

def make_pair_perms_rec(perm_size, data_possible, actual_perm):
    if perm_size == 0:
        return [ actual_perm ]
    res = []
    new_data_possible = data_possible.copy()
    for val in data_possible:
        new_perm = actual_perm.copy()
        new_perm.append(val)
        new_data_possible = new_data_possible.copy()
        new_data_possible.remove(val)
        res += make_pair_perms_rec(perm_size - 1, new_data_possible, new_perm)
    return res

def make_pair_perms(nb_pair, possible_prime):
    return make_pair_perms_rec(nb_pair, possible_prime, [])

def check_pair_set_perm(nb_pair, perm, prime_pair):
    for i in range(nb_pair):
        for j in range(i + 1, nb_pair):
            prime_i = perm[i]
            prime_j = perm[j]
            if prime_j not in prime_pair[prime_i]:
                return False
    return True

def check_pair_set(nb_pair, prime_pair, last_prime):
    possible_prime = [ last_prime ]
    for prime in prime_pair[last_prime]:
        if len(set(prime_pair[last_prime]) & set(prime_pair[prime])) >= nb_pair - 2:
            possible_prime.append(prime)
    if len(possible_prime) < nb_pair:
        return None

    perms = make_pair_perms(nb_pair, sorted(possible_prime))

    for perm in perms:
        if check_pair_set_perm(nb_pair, perm, prime_pair):
            return perm
    return None


def prime_pair_set(nb_pair):
    i = 1
    primes = set()
    prime_pair = dict()
    while True:
        if is_prime(i):
            primes.add(i)
            prime_pair[i] = []

            for prime in primes:
                if prime != i:
                    concat1 = int(str(i) + str(prime))
                    concat2 = int(str(prime) + str(i))

                    if is_prime(concat1) and is_prime(concat2):
                        prime_pair[i].append(prime)
                        prime_pair[prime].append(i)
            
            if len(prime_pair[i]) >= nb_pair - 1:
                res = check_pair_set(nb_pair, prime_pair, i)
                if res is not None:
                    return res
        i += 1

print(sum(prime_pair_set(5)))