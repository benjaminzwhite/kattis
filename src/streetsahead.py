# Streets Ahead
# https://open.kattis.com/problems/streetsahead
# TAGS: logic
# CP4: 2.3e, Hash Table (map), E
# NOTES:
"""
Reading comprehension - inputs are given in the correct order:
"Driving along the country road in some direction, one sees these streets in exactly the order provided."

Also, lots of inputs (large n) so probably can improve with faster input methods
"""
n, q = map(int, input().split())

d = {}
for i in range(n):
    k = input()
    d[k] = i
    
for _ in range(q):
    k1, k2 = input().split()
    res = abs(d[k1] - d[k2]) - 1
    print(res)