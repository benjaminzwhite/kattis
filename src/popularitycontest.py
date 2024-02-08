# Popularity Contest
# https://open.kattis.com/problems/popularitycontest
# TAGS: basic, graph
# CP4: 2.4a, Graph Data Structures
# NOTES:
n, m = map(int, input().split())

res = [0] * (n+1) # CARE! 1 based indexing

for _ in range(m):
    a, b = map(int, input().split())
    res[a] += 1
    res[b] += 1

print(*(x - i for i, x in enumerate(res[1:], 1)))