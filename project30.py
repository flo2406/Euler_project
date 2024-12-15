# The limit is 6 digit because 6 * 9 ^ 5 have 6 digits and 7 * 9 ^ 5 also.
# So, the sum of all digit fifth power cannot result to 7 digits number.

# 6 * 9 ^ 5 = 354294
# 5 * 9 ^ 5 + 3 ^ 5 = 295488

def digit_fifth_power(n):
    sum = 0
    while n > 0:
        sum += (n % 10) ** 5
        n = n // 10
    return sum

def sum_all_digit_fifth_power():
    res = 0
    for n in range(10, 295488 + 1):
        sum = digit_fifth_power(n)
        if n == sum:
            res += sum
    return res

print(sum_all_digit_fifth_power())