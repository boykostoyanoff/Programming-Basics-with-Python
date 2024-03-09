n = int(input())
matrix = [[int(x) for x in input().split(', ')] for r in range(n)]

diagonal_numbers = list()
for i in range(n):
    diagonal_numbers.append(matrix[i][i])
print(f'Primary diagonal: {", ".join([str(n) for n in diagonal_numbers])}. Sum: {sum(diagonal_numbers)}')

diagonal_numbers.clear()
j = 0
for i in range(n - 1, -1, -1):
    diagonal_numbers.append(matrix[j][i])
    j += 1
print(f'Secondary diagonal: {", ".join([str(n) for n in diagonal_numbers])}. Sum: {sum(diagonal_numbers)}')