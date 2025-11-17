# Where's My Internet??
# https://open.kattis.com/problems/wheresmyinternet
# TAGS: DFS, graph
# CP4: 4.2a, Finding CCs
# NOTES:
from collections import defaultdict

N, M = map(int, input().split())

reachable = [0] * (N + 5)
seen = [0] * (N + 5)
d = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

stk = [1]
while stk:
    curr = stk.pop()
    reachable[curr] = 1
    if seen[curr]:
        continue
    seen[curr] = 1
    for adj_v in d[curr]:
        stk.append(adj_v)

connected = True
for x in range(2, N + 1):
    if not reachable[x]:
        connected = False
        print(x)

if connected:
    print("Connected")