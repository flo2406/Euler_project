def permuted_multiple(nb_mutliple):
    i = 1
    while True:
        i_str = ''.join(sorted(str(i)))
        valid = True
        for j in range(2, nb_mutliple + 1):
            j_str = ''.join(sorted(str(j * i)))
            if i_str != j_str:
                valid = False
                break
        if valid:
            return i
        i += 1


print(permuted_multiple(6))
            
