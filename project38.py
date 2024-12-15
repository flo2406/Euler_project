def test_pandigital(n_str):
    return sorted(n_str) == [ '1', '2', '3', '4', '5', '6', '7', '8', '9']

# There is max 9 operations (if we take number 1)
# We can take number > 10000 (1 * 10000 = 10000 / 2 * 10000 = 20000 so 1000020000 (10 digits))


def max_pandigital_multitple():
    res = 0
    for num in range(1, 10000):
        val = ''
        for op in range(1, 10):
            val = val + str(num * op)
            val_len = len(val)
            if val_len < 9:
                continue
            elif val_len > 9:
                break
            else:
                if test_pandigital(val):
                    res = max(res, int(val))
    return res

print(max_pandigital_multitple())