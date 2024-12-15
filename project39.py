# First soluce

def integer_right_triangle():
    nb_sol = 0
    res = 0
    for p in range(1, 1001):
        local_sol = 0
        # Consider a as the hypothenus
        # A least 1/3 p and max 2/3 p
        for a in range(p // 3, 2 * (p // 3)):
            # b is stop to p - a else c is negatif
            stop = min(a, p - a)
            for b in range(1, stop):
                c = p - a - b
                if c > a:
                    continue
            
                if a ** 2 == b ** 2 + c ** 2:
                    local_sol += 1
                    break
        if local_sol > nb_sol:
            nb_sol = local_sol
            res = p
    return res

#print(integer_right_triangle())

# Second soluce

import math

def integer_right_triangle_v2():
    perimeter = [ 0 ] * 1001

    for a in range(1,500):
        for b in range(a,500):  
            c = int(math.sqrt(a * a + b * b))
            if a * a + b * b == c * c:
                  if a + b + c < 1000:
                       perimeter[a + b + c] += 1

    nb_sol = 0
    res = 0
    for i, sol in enumerate(perimeter):
        if sol > nb_sol:
            nb_sol = sol
            res = i
    return res

print(integer_right_triangle_v2())