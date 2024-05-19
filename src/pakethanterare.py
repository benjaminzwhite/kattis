# Packagemanager
# https://open.kattis.com/problems/pakethanterare
# TAGS: dict
# CP4: 2.3e, Hash Table (map), E
# NOTES:
packagetypes, stores = map(int, input().split())

each_store = list(map(int, input().split()))

d = {}
for _ in range(packagetypes):
    k, v = input().split()
    v = int(v)
    d[k] = v

for i in range(stores):
    cnt = 0
    for _ in range(each_store[i]):
        t, c = input().split()
        c = int(c)
        cnt += d[t] - c
    print(cnt)