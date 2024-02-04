# Križaljka
# https://open.kattis.com/problems/krizaljka
# TAGS: array, grid
# CP4: 1.6n, Output Formatting, E
# NOTES:
"""
CARE! If you use a generator (to be more ~pYtHoNic~) instead of 2 nested loops, make sure you handle the inner and outer loops correctly:

You want the "first letter in a that is also contained in b" so loop over letters of a FIRST then for each, check all of b's letters
"""
a, b = input().split()

C, R = len(a), len(b)

board = [['.'] * C for _ in range(R)]

r, c = next((row, col) for col, x in enumerate(a) for row, y in enumerate(b) if x == y)

board[r] = list(a)

for i in range(R):
    board[i][c] = b[i]

for x in board:
    print(''.join(x))