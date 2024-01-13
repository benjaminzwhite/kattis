# Cudoviste
# https://open.kattis.com/problems/cudoviste
# TAGS: array, grid
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
R, C = map(int, input().split())

M = []

for _ in range(R):
    M.append(input())
    
res = [0] * 5

for r in range(R - 1):
    for c in range(C - 1):
        free, car = 0, 0
        for cell in (M[r][c], M[r+1][c], M[r][c+1], M[r+1][c+1]):
            if cell == '.':
                free += 1
            elif cell == 'X':
                car += 1
            if free + car == 4:
                res[car] +=1

for i in res:
    print(i)