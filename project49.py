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

def prime_permutations():
    primes = dict()
    for i in range(1000, 10000):
        if is_prime(i):
            little_perm = ''.join(sorted(str(i)))
            if primes.get(little_perm):
                primes[little_perm].append(i)
            else:
                primes[little_perm] = [ i ]
    return primes
        
    
def get_arithmetic_prime_perm():
    primes = prime_permutations()
    res = []
    for prime_perm in primes.values():
        prime_perm_len = len(prime_perm)
        for i in range(prime_perm_len):
            for j in range(i + 1, prime_perm_len):
                diff = prime_perm[j] - prime_perm[i]
                for k in range(j + 1, prime_perm_len):
                    diff2 = prime_perm[k] - prime_perm[j]
                    if diff == diff2:
                        res.append({ prime_perm[i], prime_perm[j], prime_perm[k] })
    return res

print(get_arithmetic_prime_perm())
        