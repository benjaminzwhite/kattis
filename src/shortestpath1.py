# Single source shortest path, non-negative weights
# https://open.kattis.com/problems/shortestpath1
# TAGS: priority queue
# CP4: 4.4a, SSSP, BFS, Easier
# NOTES:
"""
Dijkstra's algorithm
"""
from heapq import heappush, heappop

while True:
    n, m, q, s = map(int, input().split())
    if n == m == q == s == 0:
        break

    dist = [float('inf')] * n
    dist[s] = 0

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    pq = []
    heappush(pq, (0, s)) # (weight, vertex)

    while pq:
        weight, vertex = heappop(pq)
        if weight > dist[vertex]:
            continue

        for vertex_, weight_ in adj[vertex]:
            if dist[vertex] + weight_ < dist[vertex_]:
                dist[vertex_] = dist[vertex] + weight_
                heappush(pq, (dist[vertex_], vertex_))

    for _ in range(q):
        query = int(input())
        if dist[query] < float('inf'):
            print(dist[query])
        else:
            print("Impossible")
            