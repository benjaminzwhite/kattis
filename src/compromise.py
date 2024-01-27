# Best Compromise
# https://open.kattis.com/problems/compromise
# TAGS: array
# CP4: 2.2c, 2D Array, Easier
# NOTES:
"""
Reading comprehension:
- Basically just find the most "votes" i.e. either 1/0 in zip of several strings of binary numbers
"""
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    xs = []
    
    for _ in range(n):
        xs.append(input())
    
    res = ''.join(max(col, key=col.count) for col in zip(*xs))
    print(res)