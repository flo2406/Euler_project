import math

def e_seq(n):
    res = []
    for i in range(1, (n // 3) + 2):
        res.append(1)
        res.append(2 * i)
        res.append(1)
    return res[:n - 1]

def e_convergent(n):
    if n <= 0:
        return None

    seq = e_seq(n)
    seq_len = len(seq)
    first_nb = 2

    num = 0
    den = 1

    if seq_len != 0:
        num = 1
        den = seq[-1]
        seq.pop()
        for e in seq[::-1]:
            next_num = den
            next_den = num + e * den
            num = next_num
            den = next_den
    
    num += first_nb * den
    return num, den

def sum_digit_num_e_convergent(n):
    num, den = e_convergent(n)
    res = 0
    while num > 0:
        res += num % 10
        num = num // 10
    return res

print(sum_digit_num_e_convergent(100))