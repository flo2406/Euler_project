def totient_1_to_n(n):
    totient_res = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if totient_res[i] == i:
            for j in range(i, n + 1, i):
                totient_res[j] -= int(totient_res[j] / i)

    res = 2
    min_ratio = 2 / totient_res[2]
    for i in range(3, n + 1):
        ratio = i / totient_res[i]
        if ratio < min_ratio and sorted(str(i)) == sorted(str(totient_res[i])):
            res = i
            min_ratio = ratio

    return res, min_ratio

print(totient_1_to_n(10 ** 7))
