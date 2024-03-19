size = 5
matrix = list()
targets = 0
targets_shot = list()
my_x = 0
my_y = 0

for r in range(size):
    matrix.append(input().split())
    for c in range(size):
        el = matrix[r][c]
        if el == 'A':
            my_x = r
            my_y = c
            matrix[r][c] = '.'
        elif el == 'x':
            targets += 1

targets_left = targets

commands = int(input())


def get_next_location(d, x, y, s):
    if d == 'up':
        x -= s
    elif d == 'down':
        x += s
    elif d == 'left':
        y -= s
    elif d == 'right':
        y += s
    return x, y


for _ in range(commands):
    command_info = input().split(' ')
    action = command_info[0]
    direction = command_info[1]

    if action == 'move':
        steps = int(command_info[2])
        next_x, next_y = get_next_location(direction, my_x, my_y, steps)
        if 0 <= next_x < size and 0 <= next_y < size:
            if matrix[next_x][next_y] == '.':
                my_x = next_x
                my_y = next_y
    elif action == 'shoot':
        bullet_x, bullet_y = my_x, my_y
        while True:
            bullet_x, bullet_y = get_next_location(direction, bullet_x, bullet_y, 1)
            if not (0 <= bullet_x < size and 0 <= bullet_y < size):
                break
            if matrix[bullet_x][bullet_y] == 'x':
                targets_left -= 1
                matrix[bullet_x][bullet_y] = '.'
                targets_shot.append([bullet_x,bullet_y])
                break
    if targets_left == 0:
        break

if targets_left == 0:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f'Training not completed! {targets_left} targets left.')

for t in targets_shot:
    print(t)
