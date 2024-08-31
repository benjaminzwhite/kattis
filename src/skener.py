# Skener
# https://open.kattis.com/problems/skener
# TAGS: array, grid
# CP4: 1.6n, Output Formatting, E
# NOTES:
R, C, zr, zc = map(int, input().split())

lines = []

for _ in range(R):
    lines.append(input())
    
res = '\n'.join('\n'.join(''.join(zc * c for c in line) for _ in range(zr)) for line in lines)

print(res)