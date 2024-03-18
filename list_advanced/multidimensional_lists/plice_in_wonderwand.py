size = int(input())
tea_bags_needed = 10
alice_x = 0
alice_y = 0
wonderland = list()


def move_left(x, y):
    return x, y - 1


def move_right(x, y):
    return x, y + 1


def move_up(x, y):
    return x - 1, y


def move_down(x, y):
    return x + 1, y


directions = {'up': move_up,
              'down': move_down,
              'left': move_left,
              'right': move_right}

for r in range(size):
    wonderland.append(list())
    line = input().split(' ')
    for c in range(size):
        el = line[c]
        if el == 'A':
            alice_x = r
            alice_y = c
            el = '*'
        wonderland[r].append(el)
while True:
    direction = input()
    next_x = alice_x
    next_y = alice_y
    next_x, next_y = directions[direction](next_x, next_y)

    if not 0 <= next_x < size or not 0 <= next_y < size:
        print(f"Alice didn't make it to the tea party.")
        break
    if wonderland[next_x][next_y] == 'R':
        wonderland[next_x][next_y] = '*'
        print(f"Alice didn't make it to the tea party.")
        break
    alice_x, alice_y = next_x, next_y
    if wonderland[alice_x][alice_y] in ['.', '*']:
        pass
    else:
        tea_bags_needed -= int(wonderland[alice_x][alice_y])
    wonderland[alice_x][alice_y] = '*'
    if tea_bags_needed <= 0:
        print(f"She did it! She went to the party.")
        break

for r in wonderland:
    print(*r, ' ')