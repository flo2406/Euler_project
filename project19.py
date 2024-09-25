from enum import Enum

# First soluce

class Day(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class Month(Enum):
    JANUARY = 0
    FEBRUARY = 1
    MARCH = 2
    APRIL = 3
    MAY = 4
    JUNE = 5
    JULY = 6
    AUGUST = 7
    SEPTEMBER = 8
    OCTOBER = 9
    NOVEMBER = 10
    DECEMBER = 11

def year_is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def month_size(month, year):
    if month == Month.FEBRUARY:
        if year_is_leap(year):
            return 29
        return 28

    if month in [ Month.APRIL, Month.JUNE, Month.SEPTEMBER, Month.NOVEMBER ]:
        return 30

    return 31


def count_sundays():
    res = 0
    day = Day.MONDAY
    for year_i in range(101):
        year = 1900 + year_i
        for month in Month:
            size = month_size(month, year)
            day = Day((day.value + size) % 7)

            if day == Day.SUNDAY and year_i != 0:
                res += 1
    
    return res

print(count_sundays())