rows, cols = [int(n) for n in input().split(' ')]

lair = list()
start_x = None
start_y = None
is_dead = False
message = ' '

for r in range(rows):
    row_string = input()
    lair.append(list())
    for c in range(cols):
        lair[r].append(row_string[c])
        if lair[r][c] == 'P':
            start_x = r
            start_y = c

moves = input()


def is_valid_move(next_x, next_y):
    if 0 <= next_x < rows and 0 <= next_y < cols:
        return True
    return False


for i in range(len(moves)):
    direction = moves[i]
    next_x = start_x
    next_y = start_y
    if direction == 'U':
        next_x -= 1
    elif direction == 'D':
        next_x += 1
    elif direction == 'L':
        next_y -= 1
    elif direction == 'R':
        next_y += 1
    if is_valid_move(next_x, next_y):
        lair[start_x][start_y] = '.'
        start_x = next_x
        start_y = next_y
    else:
        message = f'won: {start_x} {start_y}'
        lair[start_x][start_y] = '.'
    bunnies_location = list()
    for r in range(rows):
        for c in range(cols):
            if lair[r][c] == 'B':
                if is_valid_move(r - 1, c):
                    bunnies_location.append((r - 1, c))
                if is_valid_move(r + 1, c):
                    bunnies_location.append((r + 1, c))
                if is_valid_move(r, c - 1):
                    bunnies_location.append((r, c - 1))
                if is_valid_move(r, c + 1):
                    bunnies_location.append((r, c + 1))
    for r, c in bunnies_location:
        lair[r][c] = 'B'

    if lair[start_x][start_y] == 'B':
        message = f"dead: {start_x} {start_y}"


    if message.split(':')[0] == "dead" or message.split(':')[0] == "won":
        break

for r in range(rows):
    print(*lair[r], sep='')
print(message)