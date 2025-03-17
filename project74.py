def fact(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def sum_fact_digit(val, pre_calculated_fact):
    res = 0
    while val > 0:
        res += pre_calculated_fact[val % 10]
        val = val // 10
    return res

def digit_fact_chain(val, pre_calculated_fact, chain_len_buff):
    init_val = val
    chain = [ val ]
    val = sum_fact_digit(val, pre_calculated_fact)
    while val not in chain:
        if val < init_val:
            return len(chain) + chain_len_buff[val]
        chain.append(val)
        val = sum_fact_digit(val, pre_calculated_fact)

    return len(chain)

def nb_n_digit_fact_chains(n, limit):
    pre_calculated_fact = [ fact(i) for i in range(10) ]

    chain_len_buff = [ 0 ] * (limit + 1)

    res = 0
    for i in range(limit + 1):
        chain_len = digit_fact_chain(i, pre_calculated_fact, chain_len_buff)
        chain_len_buff[i] = chain_len
        if chain_len == n:
            res += 1
    
    return res


print(nb_n_digit_fact_chains(60, 10 ** 6))