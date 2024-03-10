rows, cols = [int(n) for n in input().split(' ')]

matrix = [[s for s in input().split(' ')] for r in range(rows)]
result = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        characters = {matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]}
        if len(characters) == 1:
            result += 1
print(result)
