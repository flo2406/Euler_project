import math

def is_perfect_square(n):
    return math.sqrt(n) == int(math.sqrt(n))

# y = x (x + 1) / 2
# 2y = x (x + 1)
# x^2 + x - 2y = 0
# delta = 1 - 4 * 1 * - 2y = 8y + 1 
# x1 = (- 1 - sqrt(8y + 1)) / (2 * 1) / x2 = (- 1 + sqrt(8y + 1)) / (2 * 1)
# x1 is negative so x = (sqrt(8y + 1) - 1) / 2
# Moreover 8y + 1 is odd so sqrt(8y + 1) is odd and sqrt(8y + 1) is even
# Dont need to check divisibility by 2
def is_triangle(n):
    return is_perfect_square(8 * n + 1)


def is_square(n):
    return is_perfect_square(n)


# y = x (3x - 1) / 2
# 2y = x (3x - 1)
# 3x^2 - x - 2y = 0
# delta = 1 - 4 * 3 * - 2y = 24y + 1 
# x1 = (1 - sqrt(24y + 1)) / (2 * 3) / x2 = (1 + sqrt(24y + 1)) / (2 * 3)
# x1 is negative so x = (sqrt(24y + 1) + 1) / 6
def is_pentagonal(n):
    delta = is_perfect_square(24 * n + 1)
    div_6 = (math.sqrt(24 * n + 1) + 1) % 6 == 0
    return delta and div_6


# y = x (2x - 1)
# 2x^2 - x - y = 0
# delta = 1 - 4 * 2 * - y = 8y + 1 
# x1 = (1 - sqrt(8y + 1)) / (2 * 2) / x2 = (1 + sqrt(8y + 1)) / (2 * 2)
# x1 is negative so x = (sqrt(8y + 1) + 1) / 4
def is_hexagonal(n):
    delta = is_perfect_square(8 * n + 1)
    div_4 = (math.sqrt(8 * n + 1) + 1) % 4 == 0
    return delta and div_4


# y = x (5x - 3) / 2
# 2y = x (5x - 3)
# 5x^2 - 3x - 2y = 0
# delta = 9 - 4 * 5 * - 2y = 40y + 9
# x1 = (3 - sqrt(40y + 9)) / (2 * 5) / x2 = (3 + sqrt(40y + 9)) / (2 * 5)
# x1 is negative so x = (sqrt(40y + 9) + 3) / 10
def is_heptagonal(n):
    delta = is_perfect_square(40 * n + 9)
    div_10 = (math.sqrt(40 * n + 9) + 3) % 10 == 0
    return delta and div_10

# y = x (3x - 2)
# 3x^2 - 2x - y = 0
# delta = 4 - 4 * 3 * - y = 12y + 4
# x1 = (2 - sqrt(12y + 4)) / (2 * 3) / x2 = (2 + sqrt(12y + 4)) / (2 * 3)
# x1 is negative so x = (sqrt(12y + 4) + 2) / 6
def is_octagonal(n):
    delta = is_perfect_square(12 * n + 4)
    div_6 = (math.sqrt(12 * n + 4) + 2) % 6 == 0
    return delta and div_6


def get_cyclical_numbers_rec(figure, actual_res, figure_used):
    actual_res_len = len(actual_res)
    need_to_start_with = ""

    if actual_res_len != 0:
        need_to_start_with = actual_res[-1][2:]

    # Result potentially detected
    if actual_res_len >= 6:
        if actual_res[-1][2:] == actual_res[0][:2]:
            return actual_res, figure_used
        return None
    
    for element in figure:
        if element in figure_used:
            continue
        for val in figure[element]:
            if val.startswith(need_to_start_with):
                new_res = actual_res.copy()
                new_res.append(val)
                new_figure_used = figure_used.copy()
                new_figure_used.append(element)
                result = get_cyclical_numbers_rec(figure, new_res, new_figure_used)
                if result != None:
                    return result
    return None

def get_cyclical_numbers(figure):
    return get_cyclical_numbers_rec(figure, [], [])


def cyclical_figurate_number():

    figure = dict()
    figure["triangle"] = []
    figure["square"] = []
    figure["pentagonal"] = []
    figure["hexagonal"] = []
    figure["heptagonal"] = []
    figure["octagonal"] = []


    for i in range(1000, 10000):
        if is_triangle(i):
            figure["triangle"].append(str(i))
        if is_square(i):
            figure["square"].append(str(i))
        if is_pentagonal(i):
            figure["pentagonal"].append(str(i))
        if is_hexagonal(i):
            figure["hexagonal"].append(str(i))
        if is_heptagonal(i):
            figure["heptagonal"].append(str(i))
        if is_octagonal(i):
            figure["octagonal"].append(str(i))

    res, figure_res = get_cyclical_numbers(figure)
    print(res)
    print(figure_res)
    return sum(map(lambda x: int(x), res))


print(cyclical_figurate_number())