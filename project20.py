# First soluce

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sum_digit(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digit(n // 10)

def factorial_sum_digit(n):
    return sum_digit(factorial(n))

print(factorial_sum_digit(100))