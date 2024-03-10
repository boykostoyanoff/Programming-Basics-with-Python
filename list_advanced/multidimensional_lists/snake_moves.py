rows, cols = [int(n) for n in input().split(" ")]
snake = input()
snake = (rows * cols // len(snake) + 1) * snake
start = 0

for rows in range(rows):
    row_snake = snake[start:start + cols]
    if rows % 2 == 1:
        row_snake = row_snake[::-1]
    print(row_snake)
    start += cols