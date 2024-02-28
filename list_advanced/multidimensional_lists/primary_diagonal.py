rows = int(input())
matrix = [[int(x) for x in input().split(' ')] for r in range(rows)]
resut = [matrix[x][x] for x in range(rows)]
print(sum(resut))