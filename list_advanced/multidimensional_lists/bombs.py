size = int(input())
matrix = [[int(n) for n in input().split(' ')] for row in range(size)]

bombs_location = [l for l in input().split(' ')]
bombs = [(int(bombs_location[i].split(',')[0]), int(bombs_location[i].split(',')[1])) for i in range(len(bombs_location))]


def is_dead_cell(number):
    if number <= 0:
        return True
    return False


for x, y in bombs:
    if not is_dead_cell(matrix[x][y]):
        power = matrix[x][y]
        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if 0 <= row < size and 0 <= col < size:
                    if not is_dead_cell(matrix[row][col]):
                        matrix[row][col] -= power
        matrix[x][y] = 0
alive_cells = 0
alive_cells_sum = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            alive_cells += 1
            alive_cells_sum += matrix[row][col]
print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
for row in range(size):
    print(*matrix[row], sep=' ')