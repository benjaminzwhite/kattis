# Perket
# https://open.kattis.com/problems/perket
# TAGS: bitmask
# CP4: 3.2f, Iterative (Combination)
# NOTES:
"""
Implementation with a bitmask to iterate over all subsets.

CARE! here though we DO NOT WANT TO ITERATE OVER EMPTY SUBSET
so range is (1, 1<<N) rather than (0, 1<<N), i.e. we skip the empty subset's bitmask 0000000....
"""
N = int(input())

ts = []
for _ in range(N):
    s, b = map(int, input().split())
    ts.append((s, b))

best = float('inf')

for mask in range(1, 1 << N): # start at 1 since empty subset not allowed
    sour, bitter = 1, 0
    for i in range(N):
        if mask & (1 << i):
            sour *= ts[i][0]
            bitter += ts[i][1]
    best = min(best, abs(sour - bitter))
    
print(best)