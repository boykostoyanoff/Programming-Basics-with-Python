matrix = []
for row in range(3):
    line = input().split(' ')
    matrix.append(line)

wining_symbol = '0'

for row in range(3):
    if matrix[row][0] == matrix[row][1] == matrix[row][2]:
        wining_symbol = matrix[row][0]
        break
    if matrix[0][row] == matrix[1][row] == matrix[2][row]:
        wining_symbol = matrix[0][row]
        break

if wining_symbol == '0':
    if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
        wining_symbol = matrix[1][1]


if wining_symbol == '0':
    print('Draw!')
elif wining_symbol == '1':
    print('First player won')
elif wining_symbol == '2':
    print('Second player won')
