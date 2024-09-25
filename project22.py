# First soluce

def score_name(str):
    sum = 0
    for c in str:
        sum += ord(c) - ord('A') + 1
    return sum

def get_all_score_name(filename):
    total_score = 0

    with open(filename, "r") as f:
        name_arr = f.read().replace("\"", "").split(",")

        name_arr.sort()

        name_arr_len = len(name_arr)
        for i in range(name_arr_len):
            total_score += (i + 1) * score_name(name_arr[i])

    return total_score

print(get_all_score_name("names.txt"))