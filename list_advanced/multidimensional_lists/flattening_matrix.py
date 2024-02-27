rows = int(input())
matrix = list()
for x in range(rows):
        matrix.append([int(n) for n in input().split(', ')])

print([x for y in matrix for x in y])