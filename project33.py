def check_digit_cancelling_frac(num, den):
    num_str = str(num)
    num_den = str(den)

    frac = num /den

    # Avoid division by zero
    if num_str[0] == num_den[0] and num_den[1] != '0':
        if int(num_str[1]) / int(num_den[1]) == frac:
            return True

    elif num_str[0] == num_den[1]:
        if int(num_str[1]) / int(num_den[0]) == frac:
            return True
        
    # Avoid division by zero
    elif num_str[1] == num_den[0] and num_den[1] != '0':
        if int(num_str[0]) / int(num_den[1]) == frac:
            return True

    # Avoid trivial fractions
    elif num_str[1] == num_den[1] and num_str[1] != '0':  
        if int(num_str[0]) / int(num_den[0]) == frac:
            return True
    
    return False

def pgcd(n, m):
    while m != 0:
        t = m
        m = n % m
        n = t
    return n

def digit_cancelling_frac():
    num_product = 1
    den_product = 1
    for num in range(10, 100):
        for den in range(num + 1, 100):
            res = check_digit_cancelling_frac(num, den)
            if res:
                num_product *= num
                den_product *= den
    div = pgcd(num_product, den_product)
    print(num_product)
    print(den_product)
    return den_product // div

print(digit_cancelling_frac())