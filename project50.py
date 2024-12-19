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

def list_primes_sum(limit):
    list_sum = [2]
    nb_cons_prime = 1
    res_prime = 2
    start_index = 0
    for n in range(3, limit):
        if is_prime(n):
            list_sum.append(n)
            list_sum_len = len(list_sum)
            next_start_index = 0
            for i in range(start_index, list_sum_len - nb_cons_prime):
                next_start_index = i
                list_sum[i] += n
                if list_sum[i] > limit:
                    start_index = i + 1
                    continue
                if is_prime(list_sum[i]):
                    res_prime = list_sum[i]
                    nb_cons_prime = list_sum_len - i
                    break
            for i in range(next_start_index + 1, list_sum_len - 1):
                list_sum[i] += n
    return res_prime, nb_cons_prime

print(list_primes_sum(1000000))