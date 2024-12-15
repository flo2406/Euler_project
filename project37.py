from queue import Queue

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

def check_truncatable_prime(str_n):
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:-i])):
            return False
        if not is_prime(int(str_n[i:])):
            return False
    return is_prime(int(str_n))

def get_truncatable_prime():
    q_prime = Queue()
    for i in range(10):
        if is_prime(i):
            q_prime.put(str(i))

    res = set()
    while not q_prime.empty():
        val = q_prime.get()
        for i in range(10):
            new_val1 = val + str(i)
            if check_truncatable_prime(new_val1):
                res.add(int(new_val1))
                q_prime.put(new_val1)
            elif is_prime(int(new_val1)):
                q_prime.put(new_val1)

            new_val2 = str(i) + val
            if check_truncatable_prime(new_val2):
                res.add(int(new_val2))
                q_prime.put(new_val2)
            elif is_prime(int(new_val2)):
                q_prime.put(new_val2)

        if (len(res) == 11):
            break
    return res

print(sum(get_truncatable_prime()))