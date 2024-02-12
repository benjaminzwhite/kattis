# Safe Houses
# https://open.kattis.com/problems/safehouses
# TAGS: brute force, grid
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
N = int(input())

board = []
for _ in range(N):
    board.append(input())

houses, spies = set(), set()

for r, row in enumerate(board):
    for c, cell in enumerate(row):
        if cell == 'S':
            spies.add((r, c))
        elif cell == 'H':
            houses.add((r, c))

res = 0

for r, c in spies:
    res = max(res, min(abs(r - r_) + abs(c - c_) for r_, c_ in houses))

print(res)