rows, cols = [int(n) for n in input().split(' ')]
matrix = [[el for el in input().split(' ')] for r in range(rows)]
message = 'Invalid input!'


def is_valid_command(command_info, rows, cols):
    if not command_info[0] == "swap":
        return False
    if not len(command_info) == 5:
        return False
    for i in range(1, 5):
        if not command_info[i].isdigit():
            return False
    x1 = int(command_info[1])
    y1 = int(command_info[2])
    x2 = int(command_info[3])
    y2 = int(command_info[4])
    if not 0 <= x1 < rows:
        return False
    if not 0 <= x2 < rows:
        return False
    if not 0 <= y1 < cols:
        return False
    if not 0 <= y2 < cols:
        return False
    return True


while True:
    command_info = input()
    if command_info == "END":
        break
    command_info = command_info.split(' ')
    if is_valid_command(command_info, rows, cols):
        x1 = int(command_info[1])
        y1 = int(command_info[2])
        x2 = int(command_info[3])
        y2 = int(command_info[4])

        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
        for i in range(rows):
            print(*matrix[i], sep=' ')
    else:
        print(message)