# Island Hopping
# https://open.kattis.com/problems/islandhopping
# TAGS: graph, tree, MST, improve
# CP4: 4.3a, MST, Standard
# NOTES:
"""
TODO: IMPROVE: my submission is at 2secs+ while some are 0.3 so my approach/implementation must have things to improve

---

This is Prim's algorithm approach
Solution below based on reading p217 Halim book and implementing as he describes it.

My first submit was with Kruskal but it gets TLE
-> read about why: for DENSE GRAPHS Prim's is faster (see notes)
"""
from queue import PriorityQueue

T = int(input())
for _ in range(T):
    V = int(input())
    xs = []
    for _ in range(V):
        x, y = map(float, input().split())
        xs.append((x, y))

    seen = [False] * V
    vertices_used = 0
    res = 0

    pq = PriorityQueue()

    # start from vertex 0
    x0, y0 = xs[0]
    seen[0] = True
    for j in range(V):
        x2, y2 = xs[j]
        d = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
        pq.put((d, j))

    while not pq.empty():
        d, j = pq.get()
        if seen[j]:
            continue
        seen[j] = True
        res += d
        vertices_used += 1
        if vertices_used == V - 1:
            break

        xj, yj = xs[j]

        for k in range(V):
            if not seen[k]:
                xk, yk = xs[k]
                d = ((xj - xk) ** 2 + (yj - yk) ** 2) ** 0.5
                pq.put((d, k))

    print(res)
