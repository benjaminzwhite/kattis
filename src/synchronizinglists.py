# Synchronizing Lists
# https://open.kattis.com/problems/synchronizinglists
# TAGS: array, sorting
# CP4: 3.3a, Binary Search
# NOTES:
"""
You can just store the original index of x (before sorting xs) and compute
final res by referring to that index.
"""
while True:
    n = int(input())
    if n == 0:
        break
    
    xs = []
    for i in range(n):
        x = int(input())
        xs.append((x, i))
    
    ys = []
    for _ in range(n):
        ys.append(int(input()))
    
    xs = sorted(xs)
    ys = sorted(ys)
    res = [-1] * n
    
    for (_, i), y in zip(xs, ys):
        res[i] = y
    
    for r in res:
        print(r)
    
    print()