# Mylla
# https://open.kattis.com/problems/mylla2
# TAGS: array
# CP4: 2.2d, 2D Array, Medium
# NOTES:
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

board = ""
for _ in range(3):
    board += input()

if any(all(board[i] == 'O' for i in line) for line in LINES):
    print("Jebb")
else:
    print("Neibb")