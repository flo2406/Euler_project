# First soluce

from enum import Enum

class Direction(Enum):
    RIGHT = 0,
    LEFT = 1,
    UP = 2,
    DOWN = 3

def create_spiral_array(n):
    array = [[0 for _ in range(n)] for _ in range(n)]
    dir = Direction.LEFT

    x = n
    y = 0
    i = n * n

    while i != 0:
        if dir == Direction.LEFT:
            if x == 0 or array[y][x - 1] != 0:
                dir = Direction.DOWN
            else:
                x = x - 1
                array[y][x] = i
                i -= 1
        elif dir == Direction.DOWN:
            if y == n - 1 or array[y + 1][x] != 0:
                dir = Direction.RIGHT
            else:
                y = y + 1
                array[y][x] = i
                i -= 1
        elif dir == Direction.RIGHT:
            if x == n - 1 or array[y][x + 1] != 0:
                dir = Direction.UP
            else:
                x = x + 1
                array[y][x] = i
                i -= 1
        else : # Direction.UP
            if y == 0 or array[y - 1][x] != 0:
                dir = Direction.LEFT
            else:
                y = y - 1
                array[y][x] = i
                i -= 1

    return array

def sum_diag(n):
    res = 0

    array = create_spiral_array(n)

    for i in range(n):
        res += array[i][i] + array[i][n - i - 1]
    
    # Remove 1 in center who is calculate twice
    res -= 1

    return res

print(sum_diag(1001))