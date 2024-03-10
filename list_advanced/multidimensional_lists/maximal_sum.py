rows, cols = [int(n) for n in input().split(' ')]
matrix = [[int(x) for x in input().split(' ')] for r in range(rows)]
max_sum = None
numbers_list = None

for r in range(rows - 2):
    for c in range(cols - 2):
        numbers = list()
        current_sum = 0
        for j in range(3):
            current_sum += sum(matrix[r + j][c:c + 3])
            numbers.append(matrix[r + j][c:c + 3])
        if max_sum:
            if max_sum < current_sum:
                max_sum = current_sum
                numbers_list = numbers
        else:
            max_sum = current_sum
            numbers_list = numbers
print(f"Sum = {max_sum}")
for i in range(3):
    print(*numbers_list[i], sep=' ')