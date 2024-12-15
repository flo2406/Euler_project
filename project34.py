def fact(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def digit_fact(n):
    sum = 0
    while n != 0:
        sum += fact(n % 10)
        n = n // 10
    return sum

# Limit to 7 * 9! because result get only 7 digits
# 7 * 9! = 2540160

def digit_fact_sum():
    sum = 0
    for i in range(10, 2540160):
        if i == digit_fact(i):
            sum += i
    return sum

print(digit_fact_sum())