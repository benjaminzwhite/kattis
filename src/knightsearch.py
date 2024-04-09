# Knight Search
# https://open.kattis.com/problems/knightsearch
# TAGS: grid, DFS
# CP4: 6.4b, String Matching, 2D
# NOTES:
"""
Exercise set by Prof. Halim himself O_o//

Solve doing DFS on a board
"""
N = int(input())
inp = input()

board = []
for i in range(N):
    board.append(inp[N * i:N * i + N])

s = "ICPCASIASG"
LEN_S = len(s)

MOVES = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if dr * dr + dc * dc == 5]

q = []
for r, row in enumerate(board):
    for c, cell in enumerate(row):
        if cell == 'I':
            q.append((r, c, 0))

flg = False
while q:
    r, c, idx = q.pop()
    if idx == LEN_S - 1:
        flg = True
        break
    for dr, dc in MOVES:
        if 0 <= (r_ := r + dr) < N and 0 <= (c_ := c + dc) < N and board[r_][c_] == s[idx + 1]:
            q.append((r_, c_, idx + 1))

if flg:
    print("YES")
else:
    print("NO")