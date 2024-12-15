def concat_str():
    str_val = ""
    str_len = 0
    i = 1
    while True:
        tmp = str(i)
        str_val += tmp
        str_len += len(tmp)
        i += 1

        if str_len > 1000000:
            break

    return str_val

def champernowne_constant():
    str_val = concat_str()
    res1 = int(str_val[0]) * int(str_val[9]) * int(str_val[99]) * int(str_val[999])
    res2 = int(str_val[9999]) * int(str_val[99999]) * int(str_val[999999])
    return res1 * res2

print(champernowne_constant())