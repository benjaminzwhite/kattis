# Money Matters
# https://open.kattis.com/problems/moneymatters
# TAGS: graph
# CP4: 4.2a, Finding CCs
# NOTES:
n, m = map(int, input().split())

amounts = []
for _ in range(n):
    amounts.append(int(input()))

seen = [0] * n
d = {k: [] for k in range(n)}

for _ in range(m):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

flg = True
for x in range(n):
    if seen[x]:
        continue
    stk = [x]
    tmp = 0
    while stk:
        curr = stk.pop()
        if seen[curr]:
            continue
        seen[curr] = 1
        tmp += amounts[curr]
        for y in d[curr]:
            if not seen[y]:
                stk.append(y)
    if tmp != 0:
        flg = False
        break

if flg:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")