# Check than operation cannot make more than 9 digits:
# 1 * 9999 = 9999 => 9 digits
# 10 * 999 = 9990 => 9 digits
# 100 * 99  ... 

def test_mult_pandigital(n, m):
    digit_set = [0] * 10

    mult_res = n * m

    while n != 0:
        if digit_set[n % 10] != 0:
            return False
        digit_set[n % 10] += 1
        n = n // 10
    
    while m != 0:
        if digit_set[m % 10] != 0:
            return False
        digit_set[m % 10] += 1
        m = m // 10

    while mult_res != 0:
        if digit_set[mult_res % 10] != 0:
            return False
        digit_set[mult_res % 10] += 1
        mult_res = mult_res // 10

    if digit_set != [0 if i == 0 else 1 for i in range(0, 10)]:
        return False
    return True

def sum_pandigital_products():
    product_set = set()
    for i in range(10000):
        div = (10 ** (len(str(i)) - 1))
        for j in range(10000 // div):
            if i * j not in product_set:
                check = test_mult_pandigital(i, j)
                if check:
                    product_set.add(i * j)
    
    return sum(product_set)

print(sum_pandigital_products())