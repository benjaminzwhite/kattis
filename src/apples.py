# Falling Apples
# https://open.kattis.com/problems/apples
# TAGS: array
# CP4: 2.2d, 2D Array, Harder
# NOTES:
"""
Basically imagine apples, a, fall down and can be stopped by:
- obstacles '#' 
- or the ground (cf r == R-1 condition later)
"""
R, C = map(int, input().split())

grid = [input() for _ in range(R)]

res = [["."] * C for _ in range(R)]

for c, column in enumerate(zip(*grid)):
    apples = 0
    for r, cell in enumerate(column):
        if cell == 'a':
            apples += 1
            res[r][c] = '.'
        elif cell == '#':
            res[r][c] = '#'
            for dr in range(1, apples+1):
                res[r-dr][c] = 'a'
            apples = 0
        if r == R-1: # CARE! Apples reach the ground
            for dr in range(0, apples):
                res[r-dr][c] = 'a'

for x in res:
    print(''.join(x))