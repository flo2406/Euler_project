def substr_divisibility_permutations_rec(actual_res):
    # Verif divisibility directly to be more optimized
    if len(actual_res) >= 4 and int(actual_res[1:4]) % 2 != 0:
        return set()
    
    if len(actual_res) >= 5 and int(actual_res[2:5]) % 3 != 0:
        return set()
    
    if len(actual_res) >= 6 and int(actual_res[3:6]) % 5 != 0:
        return set()
    
    if len(actual_res) >= 7 and int(actual_res[4:7]) % 7 != 0:
        return set()
    
    if len(actual_res) >= 8 and int(actual_res[5:8]) % 11 != 0:
        return set()
    
    if len(actual_res) >= 9 and int(actual_res[6:9]) % 13 != 0:
        return set()
    
    if len(actual_res) == 10:
        if int(actual_res[7:10]) % 17 != 0:
            return set()
        else:
            return { int(actual_res) }
    


    res = set()
    for i in range(9 + 1):
        if str(i) in actual_res:
            continue
        new_res = actual_res + str(i)
        res = res | substr_divisibility_permutations_rec(new_res)
    return res

def substr_divisibility_sum():
    return sum(substr_divisibility_permutations_rec(""))

print(substr_divisibility_sum())