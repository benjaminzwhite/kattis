# Simone
# https://open.kattis.com/problems/simone
# TAGS: dict
# CP4: 2.3c, DAT, Others
# NOTES:
N, K = map(int, input().split())
xs = map(int, input().split())

d = {k:0 for k in range(1, K + 1)}

for x in xs:
    d[x] += 1

m = min(d.values())
res = [k for k in d.keys() if d[k] == m]

print(len(res))
print(*res)