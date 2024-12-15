import math

def get_pentagonal_number(n):
    return int(n * (3 * n - 1) / 2)

def is_pentagonal(n):
    tmp = int(math.sqrt(24 * n + 1))
    test1 = tmp * tmp == 24 * n + 1
    test2 = tmp % 6 == 5
    return test1 and test2


def minimazed_diff_pent_num(limit):
    pentagonal_numbers = []

    for i in range(1, limit):
        pentagonal_numbers.append(get_pentagonal_number(i))
        for j in range(1, i):
            # Sum of 2 pentagonal is pentagonal
            if is_pentagonal(pentagonal_numbers[i - 1] + pentagonal_numbers[j - 1]):
                diff = pentagonal_numbers[i - 1] - pentagonal_numbers[j - 1]
                # Diff of 2 pentagonal is pentagonal
                if is_pentagonal(diff):
                    return diff
    return -1

print(minimazed_diff_pent_num(10000))
