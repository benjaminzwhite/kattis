# Arrangement
# https://open.kattis.com/problems/upprodun
# TAGS: mathematics
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Not sure about the CP4 tag; it's just a fair division/modular arithmetic question really?
"""
N = int(input())
M = int(input())

q, r = divmod(M, N)

for _ in range(r):
    print((q + 1) * '*')
for _ in range(N - r):
    print(q * '*')