# Nine Knights
# https://open.kattis.com/problems/nineknights
# TAGS: array, grid, chess
# CP4: 2.2c, 2D Array, Easier
# NOTES:
board = []

for _ in range(5):
    s = input()
    board.append(s)

def is_ok(r, c, dr, dc):
    return (0 <= r + dr < R) and (0 <= c + dc < C)

MOVES = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if (abs(dr) + abs(dc) == 3)]
R, C = 5, 5
knights = 0
flg = True

for r, row in enumerate(board):
    for c, cell in enumerate(row):
        if cell == 'k':
            knights += 1
            for move in filter(lambda args: is_ok(r, c, *args), MOVES):
                r_, c_ = r + move[0], c + move[1]
                if board[r_][c_] == 'k':
                    flg = False
                    break

print("valid" if flg and knights == 9 else "invalid")