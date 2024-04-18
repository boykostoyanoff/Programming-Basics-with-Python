rows = int(input())
cols = int(input())


def move(start_x, start_y, rows, cols):
    result = 0
    if start_x == rows - 1 and start_y == cols - 1:
        return 1
    if start_x >= rows or start_y >= cols:
        return 0
    result += move(start_x + 1, start_y, rows, cols)
    result += move(start_x, start_y + 1, rows, cols)
    return result


start_x = 0
start_y = 0
ways = 0
print(move(start_x, start_y, rows, cols))
