# First soluce

def create_all_permutations_rec(digit_done, val, permu):
    if len(digit_done) == 10:
        permu.append(val)

    for i in range(10):
        if i in digit_done:
            continue
        else:
            val = val * 10 + i
            digit_done.add(i)
            create_all_permutations_rec(digit_done, val, permu)
        val = val // 10
        digit_done.remove(i)

def create_all_permutations():
    permu = []
    create_all_permutations_rec(set(), 0, permu)
    return permu

print(create_all_permutations()[999999])