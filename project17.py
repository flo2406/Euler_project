# First soluce

def get_digit_string(digit):
    if digit < 0 or digit > 9:
        print("Val is not a digit")
    
    if digit == 0:
        return "zero"
    elif digit == 1:
        return "one"
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    else: # digit == 9
        return "nine"
    
def get_teen_string(teen):
    if teen < 10 or teen > 19:
        print("Val is not a teen")
    
    if teen == 10:
        return "ten"
    elif teen == 11:
        return "eleven"
    elif teen == 12:
        return "twelve"
    elif teen == 13:
        return "thirteen"
    elif teen == 14:
        return "fourteen"
    elif teen == 15:
        return "fifteen"
    elif teen == 16:
        return "sixteen"
    elif teen == 17:
        return "seventeen"
    elif teen == 18:
        return "eighteen"
    elif teen == 19:
        return "nineteen"

def get_ten_string(ten):
    if ten < 2 or ten > 9:
        print("Val is not a ten")
    
    if ten == 2:
        return "twenty"
    elif ten == 3:
        return "thirty"
    elif ten == 4:
        return "forty"
    elif ten == 5:
        return "fifty"
    elif ten == 6:
        return "sixty"
    elif ten == 7:
        return "seventy"
    elif ten == 8:
        return "eighty"
    elif ten == 9:
        return "ninety"

def get_number_string(val):
    if (val > 1000 or val < 0):
        print("Value is not supported")

    if (val == 1000):
        return "one thousand"
    
    # Between 0 and 9
    if val < 10:
        return get_digit_string(val)
    
    # Between 10 and 19
    if val < 20:
        return get_teen_string(val)
    
    # Between 20 and 99
    if val < 100:
        ten_digit = val // 10
        ten_str = get_ten_string(ten_digit)
        rest_str = get_number_string(val % 10)

        if rest_str != "zero":
            return ten_str + " " + rest_str
        else:
            return ten_str

    # Higher than 100
    hundred_digit = val // 100
    hundred_str = get_digit_string(hundred_digit) + " hundred"
    rest_str = get_number_string(val % 100)

    if rest_str != "zero":
        return hundred_str + " and " + rest_str
    else:
        return hundred_str
    
def get_number_string_size(val):
    return len(get_number_string(val).replace(" ", ""))

sum = 0
for i in range(1, 1001):
    print(get_number_string(i))
    sum += get_number_string_size(i)

print(sum)