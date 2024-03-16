d = int(input())
board = list()
moves = 0
for r in range(d):
    row_string = input()
    board.append(list())
    for i in range(len(row_string)):
        board[r].append(row_string[i])


def is_valid_move(r, c):
    if 0 <= r < d and 0 <= c < d:
        return True
    return False


for r in range(d):
    for c in range(d):
        if board[r][c] == 'K':
            checks = [(r + 1, c - 2), (r + 2, c - 1), (r + 2, c + 1), (r + 1, c + 2)]
            for check_r, check_c in checks:
                if is_valid_move(check_r, check_c):
                    if board[check_r][check_c] == 'K':
                        moves += 1
                        board[check_r][check_c] = '0'

print(moves)
