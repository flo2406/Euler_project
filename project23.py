# First soluce

def get_sum_divisor(n):
    res = 1 # 1 is always divisor and n is not consider as divisor of n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res += i
            if i != n // i:
                res += n // i
        i += 1
    return res

def is_abundant_number(n):
    return get_sum_divisor(n) > n

def update_is_sum_of_abundant_array(abundant_set, is_sum_of_abundant, val):
    arr_size = len(is_sum_of_abundant)
    for i in abundant_set:
        if i + val < arr_size:
            is_sum_of_abundant[i + val] = True

def sum_non_abundant():
    limit = 28123

    is_sum_of_abundant = [False] * limit
    abundant_set = set()

    for i in range(1, limit):
        if is_abundant_number(i):
            abundant_set.add(i)
            update_is_sum_of_abundant_array(abundant_set, is_sum_of_abundant, i)

    sum = 0
    for i in range(1, limit):
        if not is_sum_of_abundant[i]:
            sum += i

    return sum

print(sum_non_abundant())