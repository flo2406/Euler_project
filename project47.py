# First version

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
    
def distinct_prime_factor(n):
    primes = []
    nb_succ = 0
    i = 2
    while True:
        if is_prime(i):
            nb_succ = 0
            primes.append(i)
        else:
            factors = prime_factor(i, primes)
            if len(factors) >= n:
                nb_succ += 1
            else:
                nb_succ = 0

            if nb_succ >= n:
                return i - nb_succ + 1

        i += 1
            
#print(distinct_prime_factor(4))

# Second version

def distinct_prime_factor_v2(n):
    limit = 1000000
    factors = [0] * limit # number of prime factors.
    count = 0
    for i in range(2, limit):
         # i is prime
        if factors[i] == 0:
            count = 0
            val = i
            while val < limit:
                factors[val] += 1
                val += i
        elif factors[i] >= n:
            count += 1
            if count == n:
                return i - n + 1
        else:
            count = 0

print(distinct_prime_factor_v2(4))