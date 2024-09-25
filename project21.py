# First soluce

def get_sum_divisor(n):
    res = 1 # 1 is always divisor and n is not consider as divisor of n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res += i + n // i
        i += 1
    return res

def get_amicable_numbers(limit):
    res_arr = [-1] * limit 
    for i in range(limit):
        res_arr[i] = get_sum_divisor(i)

    res_sum = 0

    for i in range(limit):
        j = res_arr[i]
        if j >= limit:
            continue

        i_bis = res_arr[j]

        if i == i_bis and i < j: # i < j to avoid i == j and to avoid to count twice the value
            res_sum += i + j
    
    return res_sum

print(get_amicable_numbers(10000))