# Fountain - also called Fontan
# https://open.kattis.com/problems/fontan
# TAGS: dfs, grid
# CP4: 4.2b, Flood Fill, Easier
# NOTES:
"""
The conditions on r and c are a bit tricky compared to usual DFS/floodfill:

If cell below is AIR '.' you can move water down but if cell below is rock '#' you can move laterally.
(Nice twist on standard 4 x/y directions)

Also there's some conditions on the last row:
i.e. you pretend the the row below the last is all air so you DO NOT FILL WIDTH WISE the last row in general.
(Hard to explain in words, just see the first test case illustration)
"""
R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(input()))

stk = [(r, c) for r in range(R) for c in range(C) if board[r][c] == 'V']
seen = set()

while stk:
    r, c = stk.pop()
    if (r, c) in seen or r >= R or c < 0 or c >= C:
        continue
    seen.add((r, c))

    board[r][c] = 'V'
    if r < R - 1 and board[r + 1][c] == '.':
        stk.append((r + 1, c))
    elif r < R - 1 and board[r + 1][c] == '#':
        if c > 0 and board[r][c - 1] == '.':
            stk.append((r, c - 1))
        if c < C - 1 and board[r][c + 1] == '.':
            stk.append((r, c + 1))

for row in board:
    print(''.join(row))