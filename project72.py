def sum_totient_1_to_n(n):
    totient_res = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if totient_res[i] == i:
            for j in range(i, n + 1, i):
                totient_res[j] -= int(totient_res[j] / i)

    return sum(totient_res[2:])

print(sum_totient_1_to_n(10 ** 6))