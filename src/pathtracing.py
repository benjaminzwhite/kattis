# Path Tracing
# https://open.kattis.com/problems/pathtracing
# TAGS: interpreter, grid
# CP4: 6.2d, Output Formatting, H
# NOTES:
"""
I was getting WA until I added .strip() to input O_o (maybe was doing input reading incorrectly)
"""
import sys

r, c = 0, 0
path = [(r, c)]

for move in sys.stdin:
    move = move.strip() # O_o ???
    if move == "down":
        r += 1
    elif move =="left":
        c -= 1
    elif move == "up":
        r -= 1
    else:
        c += 1
    path.append((r, c))

width = 1 + max(abs(t[1] - u[1]) for t in path for u in path)
height = 1 + max(abs(t[0] - u[0]) for t in path for u in path)

min_r, min_c = float('inf'), float('inf')
for (r, c) in path:
    min_r = min(r, min_r)
    min_c = min(c, min_c)

# translate all points by the vector given by min r min c so that they all fit inside top left r, c = 0, 0
# (don't know why I used ALL_CAPS for this O_o ?!)
UPDATED_PATH = [(r - min_r + 1, c - min_c + 1) for r, c in path]

res = []
res.append(['#'] * (2 + width))
for _ in range(height):
    res.append(['#'] + [' '] * width + ['#'])
res.append(['#'] * (2 + width))

start_r, start_c = UPDATED_PATH[0]
res[start_r][start_c] = 'S'
end_r, end_c = UPDATED_PATH[-1]
res[end_r][end_c] = 'E'
for (r, c) in UPDATED_PATH[1:-1]:
    if res[r][c] not in {'S', 'E'}: # dont overwrite S or E if we already know they are start and end locations
        res[r][c] = '*'

for row in res:
    print(''.join(row))