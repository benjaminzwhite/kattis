# From A to B
# https://open.kattis.com/problems/fromatob
# TAGS: BFS, greedy
# CP4: 1.4i, Still Easy
# NOTES:
"""
The greedy approach works: always try to divide by 2, else += by 1 to reach an even number.

I tried submitting a BFS approach to see check that the greedy approach
works, and the BFS was AC also; so I left the 2 different solutions here.

---

# -- 1) BFS solution approach --

a, b = map(int, input().split())

from collections import deque

q = deque([(a, 0)])
seen = set()

while q:
    x, moves = q.popleft()
    if x in seen:
        continue
    seen.add(x)

    if x == b:
        print(moves)
        break

    if x < b:
        q.append((b, moves + b - x))

    else:
        if x % 2 == 0:
            q.append((x // 2, moves + 1))
        q.append((x + 1, moves + 1))

"""
# -- 2) Greedy solution approach --
a, b = map(int, input().split())

cnt = 0
if a < b:
    cnt = b - a
else:
    while a > b:
        if a % 2 == 1:
            a += 1
            cnt += 1
        else:
            a //= 2
            cnt += 1
    if a < b:
        cnt += b - a

print(cnt)