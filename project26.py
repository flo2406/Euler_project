# First soluce

def cycle_length(denominator):
    numerator = 10
    rests = []
    rest = numerator
    while True:
        # Get rest of division between numerator and denominator
        rest = numerator % denominator
        # If rest already in list of rests => finish because, we will remake same operations
        if rest in rests:
            break
        rests.append(rest)

        # Division is terminated, there is no cycle
        if rest == 0:
            return 0

        # Else, multiply by 10 to continue
        numerator = rest * 10
        while numerator < denominator:
            numerator *= 10
    
    return len(rests) - rests.index(rest)

def get_longest_cycle(n):
    res = 0
    res_i = 0
    for i in range(2, n):
        tmp = cycle_length(i)
        if tmp > res:
            res = tmp
            res_i = i
    return res_i

print(get_longest_cycle(1000))