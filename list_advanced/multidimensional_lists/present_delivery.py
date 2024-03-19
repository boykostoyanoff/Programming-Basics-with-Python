number_of_presents = int(input())
size = int(input())
neighborhood = []
nice_kids = 0
santa_x = 0
santa_y = 0

for r in range(size):
    neighborhood.append(input().split())
    for c in range(size):
        if neighborhood[r][c] == 'S':
            santa_x = r
            santa_y = c
        if neighborhood[r][c] == 'V':
            nice_kids += 1

nice_kids_left = nice_kids


def next_move(d, x, y):
    if d == 'up':
        x = x - 1
    elif d == 'down':
        x += 1
    elif d == 'left':
        y -= 1
    elif d == 'right':
        y += 1
    return x, y


while True:
    direction = input()
    if direction == "Christmas morning":
        break

    neighborhood[santa_x][santa_y] = '-'

    santa_x, santa_y = next_move(direction, santa_x, santa_y)

    place = neighborhood[santa_x][santa_y]
    if place == 'V':
        number_of_presents -= 1
        nice_kids_left -= 1
    elif place == 'C':
        for d in ['left', 'right', 'up', 'down']:
            x, y = next_move(d, santa_x, santa_y)
            place = neighborhood[x][y]
            if place in ['V', 'X'] and number_of_presents > 0:
                number_of_presents -= 1
                if place == 'V':
                    nice_kids_left -= 1
                neighborhood[x][y] = '-'

    neighborhood[santa_x][santa_y] = 'S'

    if nice_kids_left == 0:
        break

    if number_of_presents <= 0:
        print(f"Santa ran out of presents!")
        break

for r in neighborhood:
    print(*r, sep=' ')

if nice_kids_left > 0:
    print(f"No presents for {nice_kids_left} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
