import math

def is_triangle(n):
    tmp = int(math.sqrt(8 * n + 1))
    return tmp * tmp == 8 * n + 1

def is_pentagonal(n):
    tmp = int(math.sqrt(24 * n + 1))
    test1 = tmp * tmp == 24 * n + 1
    test2 = tmp % 6 == 5
    return test1 and test2

def tri_pen_hex_number(limit):
    for i in range(2, limit):
        hex = i * (2 * i - 1)
        if is_triangle(hex) and is_pentagonal(hex):
            print(hex)
    
tri_pen_hex_number(100000)