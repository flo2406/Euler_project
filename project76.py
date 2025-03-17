def counting_summations_rec(n, val_max, list_sum):
    res = 0
    if list_sum.get((n, val_max)) != None:
        return list_sum.get((n, val_max))
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    for i in range(val_max, 0, -1):
        res += counting_summations_rec(n - i, i, list_sum)
    
    list_sum[(n, val_max)] = res
    return res
            
def counting_summations(n):
    return counting_summations_rec(n, n - 1, dict())

print(counting_summations(100))