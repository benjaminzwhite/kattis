# CD
# https://open.kattis.com/problems/cd
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
from sys import stdin

while True:
    N, M = map(int, input().split())
    if (N == 0 and M == 0):
        break
    cnt = 0
    a = set(stdin.readline() for _ in range(N))
    for _ in range(M):
        if stdin.readline() in a:
            cnt += 1
    
    print(cnt)