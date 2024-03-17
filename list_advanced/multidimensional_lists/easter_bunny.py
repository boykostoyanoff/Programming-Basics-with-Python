size = int(input())
bunny_x = None
bunny_y = None
field = []
directions = {'up': list(),
              'down': list(),
              'left': list(),
              'right': list()}
for r in range(size):
    field.append([])
    field_row = input().split(' ')
    for c in range(len(field_row)):
        el = field_row[c]
        if el == 'B':
            bunny_x = r
            bunny_y = c
        elif el == 'X':
            pass
        else:
            el = int(el)
        field[r].append(el)

for row in range(bunny_x - 1, -1, -1):
    if field[row][bunny_y] == 'X':
        break
    directions['up'].append([row, bunny_y])

for row in range(bunny_x + 1, size):
    if field[row][bunny_y] == 'X':
        break
    directions['down'].append((row, bunny_y))

for col in range(bunny_y - 1, -1, -1):
    if field[bunny_x][col] == 'X':
        break
    directions['left'].append((bunny_x, col))

for col in range(bunny_y + 1, size):
    if field[bunny_x][col] == 'X':
        break
    directions['right'].append((bunny_x, col))

best_way = 'up'
max_eggs = float('-inf')
for d, c in directions.items():
    eggs = 0
    for x, y in c:
        eggs += field[x][y]
    if max_eggs < eggs and len(c) > 0:
        max_eggs = eggs
        best_way = d
print(best_way)
for location in directions[best_way]:
    print(list(location))
print(max_eggs)
