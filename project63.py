def powerful_digit_count():
    res = 1
    for n in range(2, 10):
        e = 1
        while True:
            val = n ** e
            val_len = len(str(val))
            if val_len < e:
                break
            if val_len == e:
                res += 1
            e += 1
    return res

print(powerful_digit_count())            