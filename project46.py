import math

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

def is_square(n):
    tmp = math.sqrt(n)
    return tmp == int(tmp)

def goldbach_conjecture_fail():
    list_prime = []
    i = 3
    while True:
        if is_prime(i):
            list_prime.append(i)
        else:
            conjecture_valid = False
            for prime in list_prime:
                tmp = i - prime
                if tmp % 2 == 0 and is_square(tmp // 2):
                    conjecture_valid = True
                    break
            if not conjecture_valid:
                return i

        i += 2

print(goldbach_conjecture_fail())