invalid_message = f"Invalid coordinates"
rows = int(input())

matrix = [[int(n) for n in input().split(' ')] for r in range(rows)]
command = input().split()
while not command[0] == "END":
    action = command[0]
    r, c, value = [int(n) for n in command[1:4]]

    if 0 <= r < rows and 0 <= c < len(matrix[1]):
        if action == "Subtract":
            value *= -1
        matrix[r][c] += value
    else:
        print(invalid_message)

    command = input().split()

[print(*r) for r in matrix]