rows= int(input())
matrix = [[x for x in input()] for y in range(rows)]
symbol = input()
is_symbol = False
for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == symbol:
            print((r,c))
            is_symbol = True
            break
    if is_symbol:
        break
else:
    print(f'{symbol} does not occur in the matrix')