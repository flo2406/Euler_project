import math

## Code never terminated (but can find response)
## Response can be find with logic
## 3/7 == 428571/999999 and remove 1 to numerator

def prime_factors(n, primes):
    res = []
    for prime in primes:
        if n == 0:
            break
        while n != 0 and n % prime == 0:
            res.append(prime)
            n = n // prime
    return set(res)

def get_nearest_frac_coprime(num, min_val, max_val, limit_nb, primes):
    min_den = math.ceil(num / max_val)
    if min_val != 0:
        max_den = min(math.floor(num / min_val), limit_nb)
    else:
        max_den = limit_nb

    if min_den > max_den:
        return None

    factors = prime_factors(num, primes)

    while min_den <= max_den:
        valid = True
        for factor in factors:
            if min_den % factor == 0:
                valid = False
                break
        if valid:
            return min_den
        min_den += 1
    return None

def erathostene(n):
    era = [ False ] * (n + 1)
    era[0] = True
    era[1] = True
    i = 2
    while i * i <= n:
        if not era[i]:
            j = 2 * i
            while j <= n:
                era[j] = True
                j += i  
        i += 1
    return [i for i, x in enumerate(era) if not x]

def ordered_fraction_left(n, limit):
    res = (0, 1)
    primes = erathostene(n)
    for num in range(n, 0, -1):
        den = get_nearest_frac_coprime(num, res[0] / res[1], limit, n, primes)
        if den != None and num / den != limit:
            print(num, den)
            res = (num, den)
    return res

print(ordered_fraction_left(1000000, 3 / 7))