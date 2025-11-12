# Crop Triangles (Easy)
# https://open.kattis.com/problems/cropeasy
# TAGS: mathematics, geometry, brute force
# CP4: 7.2e, Triangles + Circles
# NOTES:
from itertools import combinations

T = int(input())
for tc in range(1, T + 1):

    n, A, B, C, D, X, Y, M = map(int, input().split())

    pts = [(X, Y)]
    for _ in range(n - 1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        pts.append((X, Y))

    cnt = 0
    for (x1, y1), (x2, y2), (x3, y3) in combinations(pts, 3):
        if (x1 + x2 + x3) % 3 == 0 and (y1 + y2 + y3) % 3 == 0:
            cnt += 1

    print(f"Case #{tc}: {cnt}")