rows, cols = [int(n) for n in input().split(', ')]
matrix = [[int(x) for x in input().split(' ')] for j in range(rows)]
print(*[sum([matrix[r][c] for r in range(rows)]) for c in range(cols)], sep='\n')
