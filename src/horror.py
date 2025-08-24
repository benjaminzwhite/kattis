# Horror List
# https://open.kattis.com/problems/horror
# TAGS: graph, BFS
# CP4: 4.4a, SSSP, BFS, Easier
# NOTES:
"""
After the reading comprehension: it's asking "which vertex is furthest away from the given list of bad vertices"
"""
from collections import deque, defaultdict

N, H, L = map(int, input().split())

is_horror = deque((x, 0) for x in input().split())

horror_index = {str(n): float('inf') for n in range(N)}

adj = defaultdict(list)
for _ in range(L):
    a, b = input().split()
    adj[a].append(b)
    adj[b].append(a)

while is_horror:
    x, hi = is_horror.popleft()
    if horror_index[x] < float('inf'):
        continue

    horror_index[x] = hi
    for y in adj[x]:
        is_horror.append((y, hi + 1))

# NOTE: Python dict stable/key creation order is 1,2,3...
# so next() will get the LOWEST ID IN CASE OF A TIE, as demanded by exercise
mv = max(horror_index.values())
res = next(k for k, v in horror_index.items() if v == mv)

print(res)