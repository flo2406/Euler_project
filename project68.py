# Magic 3 gon
# a / b / c is intern and d / e / f is extern
# d + a + b = e + b + c = f + a + c

def n_combinaison_rec(n, actual_comb):
    if len(actual_comb) == n:
        return [ actual_comb ]
 
    res = []
    for i in range(1, n + 1):
        if i in actual_comb:
            continue
        else:
            res += n_combinaison_rec(n, actual_comb + [ i ])
    return res

def n_combinaison(n):
    return n_combinaison_rec(n, [])

def magic_3_gon():
    res = None
    for comb in n_combinaison(6):
        a = comb[0]
        b = comb[1]
        c = comb[2]
        d = comb[3]
        e = comb[4]
        f = comb[5]

        if d + a + b == e + b + c and d + a + b == f + a + c:
            actual_res = [[d, a, b], [e, b, c], [f, c, a]]
            index_min = actual_res.index(min(actual_res))
            actual_res = actual_res[index_min:] + actual_res[:index_min]
            if res is None:
                res = actual_res
            else:
                res = max(res, actual_res)
    return res


# Magic 3 gon
# a / b / c / d / e is intern and f / g / h / i / j is extern
# f + a + b = g + b + c = h + c + d = i + d + e = j + e + a

def magic_5_gon():
    res = None
    combinaisons = n_combinaison(10)
    for comb in combinaisons:
        a = comb[0]
        b = comb[1]
        c = comb[2]
        d = comb[3]
        e = comb[4]
        f = comb[5]
        g = comb[6]
        h = comb[7]
        i = comb[8]
        j = comb[9]

        val_need = f + a + b
        if val_need == g + b + c and val_need == h + c + d and val_need == i + d + e and val_need == j + e + a:
            actual_res = [[f, a, b], [g, b, c], [h, c, d], [i, d, e], [j, e, a]]
            index_min = actual_res.index(min(actual_res))
            actual_res = actual_res[index_min:] + actual_res[:index_min]
            if res is None:
                res = actual_res
            else:
                res = max(res, actual_res)
    return res


print(magic_5_gon())