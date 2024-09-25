# First soluce

def fibonacci(nb_digit):
    if nb_digit < 1:
        print("Number of digit can be inferior or equal to 0")

    if nb_digit == 1:
        return 1

    index = 3
    n1 = 1
    n2 = 1
    res = n1 + n2

    while len(str(res)) < 1000:
        n2 = n1
        n1 = res
        res = n1 + n2
        index += 1
    
    return index

print(fibonacci(1000))