rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]
matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(matrix)