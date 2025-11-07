# Where's My Waterfall?
# https://open.kattis.com/problems/wheresmywaterfall
# TAGS: grid, dfs, flood fill
# CP4: 4.2b, Flood Fill, Easier
# NOTES:
R, C, k = map(int, input().split())

seen = [[False] * C for _ in range(R)]

ps = list(map(int, input().split()))

board = [list(input()) for _ in range(R)]

stk = [(0, col) for col in ps]

while stk:
    r, c = stk.pop()
    if seen[r][c]:
        continue
    seen[r][c] = True
    board[r][c] = '~'

    if r == R - 1:
        continue
    elif board[r + 1][c] == 'O':
        stk.append((r + 1, c))
    elif board[r + 1][c] in "?#":
        if c > 0 and board[r][c - 1] == 'O':
            stk.append((r, c - 1))
        if c < C - 1  and board[r][c + 1] == 'O':
            stk.append((r, c + 1))

for row in board:
    print(''.join(row))