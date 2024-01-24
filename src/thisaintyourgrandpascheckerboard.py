# This Ain't Your Grandpa's Checkerboard
# https://open.kattis.com/problems/thisaintyourgrandpascheckerboard
# TAGS: basic
# CP4: 2.2c, 2D Array, Easier
# NOTES:
"""
- Unoptimized, doesn't break early etc.
"""
N = int(input())

b = []

for _ in range(N):
    b.append(input())
    
flg = 1

for row in b:
    if row.count('W') != row.count('B') or 'BBB' in row or 'WWW' in row:
        flg = 0

for col in zip(*b):
    C = ''.join(col)
    if col.count('W') != col.count('B') or 'BBB' in C or 'WWW' in C:
        flg = 0

print(flg)