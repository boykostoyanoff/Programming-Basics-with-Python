size = int(input())
directions = input().split(' ')
collected_coals = 0

maze = [[x for x in input().split(' ')] for row in range(size)]
x = None
y = None
coals_on_map = sum([maze[i].count('c') for i in range(size)])

for r in range(size):
    for c in range(size):
        if maze[r][c] == 's':
            x = r
            y = c
            maze[x][y] = '*'
            break
    if x:
        break


def is_valid_move(next_x, next_y):
    if not 0 <= next_x < size or not 0 <= next_y < size:
        return False
    return True


for move in directions:
    next_x = x
    next_y = y
    if move == 'up':
        next_x -= 1
    elif move == 'down':
        next_x += 1
    elif move == 'right':
        next_y += 1
    elif move == 'left':
        next_y -= 1

    if is_valid_move(next_x, next_y):
        x = next_x
        y = next_y

    if maze[x][y] == 'c':
        collected_coals += 1
        if coals_on_map == collected_coals:
            print(f"You collected all coal! ({x}, {y})")
            break
        maze[x][y] = '*'
    elif maze[x][y] == 'e':
        print(f"Game over! ({x}, {y})")
        break
else:
    print(f"{coals_on_map - collected_coals} pieces of coal left. ({x}, {y})")
