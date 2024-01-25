# Prva
# https://open.kattis.com/problems/prva
# TAGS: grid
# CP4: 2.2d, 2D Array, Harder
# NOTES:
"""
- Unoptimized; don't need to keep whole words[] list, can just find minimum as you loop through rows and cols
- Python min() will indeed produce "the lexicographically smallest word" as required by exercise
"""
R, C = map(int, input().split())

board = []

for _ in range(R):
    board.append(input())

words = []

for row in board:
    words.extend(x for x in row.split('#') if len(x) > 1)

for col in zip(*board):
    words.extend(x for x in ''.join(col).split('#') if len(x) > 1)

res = min(words)

print(res)