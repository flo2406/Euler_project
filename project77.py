import math

def prime_factors(n, primes):
    res = []
    for prime in primes:
        if n == 0:
            break
        while n != 0 and n % prime == 0:
            res.append(prime)
            n = n // prime
    return res

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

def prime_summations_rec(n, val_max, list_sum, era):
    res = 0
    if list_sum.get((n, val_max)) != None:
        return list_sum.get((n, val_max))
    if n == 0:
        return 1
    elif n < 0:
        return 0
    for i in era:
        if i > val_max:
            break
        res += prime_summations_rec(n - i, i, list_sum, era)
    
    list_sum[(n, val_max)] = res
    return res
            
def prime_summations(n):
    era = erathostene(n)
    return prime_summations_rec(n, n - 1, dict(), era)

def get_prime_summations(limit):
    i = 2
    while True:
        val = prime_summations(i)
        if val > limit:
            return i, val
        i += 1

print(get_prime_summations(5000))