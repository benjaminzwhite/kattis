# EpigDanceOff
# https://open.kattis.com/problems/epigdanceoff
# TAGS: array, grid
# CP4: 2.2c, 2D Array, Easier
# NOTES:
N, M = map(int, input().split())

board = []

for _ in range(N):
    line = input()
    board.append(line)
    
spaces = 0

for col in zip(*board):
    if all(c == '_' for c in col):
        spaces += 1
        
print(1 + spaces)