n = int(input())
matrix = [[int(x) for x in input().split(' ')] for r in range(n)]

diagonal_numbers = list()
for i in range(n):
    diagonal_numbers.append(matrix[i][i])

diagonal_numbers2 = list()
j = 0
for i in range(n - 1, -1, -1):
    diagonal_numbers2.append(matrix[j][i])
    j += 1

print(abs(sum(diagonal_numbers) - sum(diagonal_numbers2)))
