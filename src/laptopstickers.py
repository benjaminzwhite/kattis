# Laptop Stickers
# https://open.kattis.com/problems/laptopstickers
# TAGS: array, grid
# CP4: 2.2c, 2D Array, Easier
# NOTES:
"""
Renamed variables L, H, K to:

(C)ols, (R)ows, (N)umber of stickers, clearer imho O_o
"""
ALPH = 'abcdefghijklmnopqrstuvwxyz'

C, R, N = map(int, input().split())

board = [['_'] * C for _ in range(R)]

xs = [input() for _ in range(N)] 

for i, line in enumerate(xs):
    w, h, c, r = map(int, line.split())
    for r_ in range(r, r + h):
        for c_ in range(c, c + w):
            if r_ < R and c_ < C:
                board[r_][c_] = ALPH[i]

for row in board:
    print(''.join(row))