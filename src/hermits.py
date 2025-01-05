# Hermits
# https://open.kattis.com/problems/hermits
# TAGS: array
# CP4: 2.4a, Graph Data Structures
# NOTES:
"""
It's just do as you are told. CARE! it is 1 based indexing.

For each pair of roads that cross, increment the "effective number of people" res[] of each road by the POPULATION COUNT cnt[] of the OTHER road.
"""
N = int(input())

cnt = [0] # 0 is sentinel, so can use 1-based indexing
cnt.extend(map(int, input().split()))

res = cnt[:] # CARE! initialize the effective number of people on road i WITH THE ACTUAL NUMBER ON THAT ROAD, cnt. Then will add the "adjacent roads" in the below loop

M = int(input())
for _ in range(M):
    s1, s2 = map(int, input().split())
    res[s1] += cnt[s2]
    res[s2] += cnt[s1]

min_val = min(res[1:]) # CARE! ignore the sentinel value in index 0

idx = next(i for i, x in enumerate(res) if x == min_val)

print(idx)