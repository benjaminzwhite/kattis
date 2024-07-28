# Lost Lineup
# https://open.kattis.com/problems/lostlineup
# TAGS: basic, array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
n = int(input())
ds = map(int, input().split())

res = [1] * n

for i, d in enumerate(ds):
    res[d + 1] = i + 2
    
print(' '.join(d for d in map(str, res)))