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

def prime_factor(n, primes):
    res = []
    for prime in primes:
        if n == 0:
            break
        while n != 0 and n % prime == 0:
            res.append(prime)
            n = n // prime
    return set(res)
    

def totient(n, primes):
    res = [ True ] * n
    res[0] = False
    factors = prime_factor(n, primes)
    for fact in factors:
        i = 1
        while i * fact < n:
            res[i * fact] = False
            i += 1
    return [i for i, val in enumerate(res) if val]


def totient_maximum_test(limit):
    res = 0
    index_res = 0
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
        else:
            list_rel_prime = totient(i, primes)
            totient_res = i / len(list_rel_prime)
            if totient_res > res:
                res = totient_res
                index_res = i
    return res, index_res

# After some test, I see that it is multiplication primes in order (logic to remove maximum of relative prime)
# 2, 6 (2 * 3), 30 (6 * 5), 210 (30 * 7), 2310 (210 * 11)

def totient_maximum(limit):
    res = 2
    i = 3
    while True:
        if is_prime(i):
            res *= i
            if res > limit:
                res = res // i
                break
        i += 1
    return res

print(totient_maximum(1000000))