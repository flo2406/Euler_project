# First soluce

def all_int_combinaison(n):
    distinct_value = set()

    for a in range(2, n + 1):
        for b in range(2, n + 1):
            distinct_value.add(a ** b)

    return len(distinct_value)

print(all_int_combinaison(100))