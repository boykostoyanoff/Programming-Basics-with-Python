rows, cols = [int(n) for n in input().split(', ')]
matrix = [[int(n) for n in input().split(', ')] for r in range(rows)]
max_sum_numbers = list()
max_sum = 0

if rows < 1 or cols < 1:
    pass
else:
    max_sum = matrix[0][0] + matrix[1][0] + matrix[0][1] + matrix[1][1]
    max_sum_numbers = [[matrix[0][0], matrix[0][1]], [matrix[1][0], matrix[1][1]]]
    for r in range(rows - 1):
        for c in range(cols - 1):
            cur_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
            if max_sum < cur_sum:
                max_sum = cur_sum
                max_sum_numbers = [[matrix[r][c], matrix[r][c + 1]], [matrix[r + 1][c], matrix[r + 1][c + 1]]]

print(*max_sum_numbers[0], sep=' ')
print(*max_sum_numbers[1], sep=' ')
print(max_sum)