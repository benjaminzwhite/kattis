# 4 thought
# https://open.kattis.com/problems/4thought
# TAGS: brute force
# CP4: 3.2a, Pre-calculate-able
# NOTES:
"""
- linked on p152 of Sannemo PDF - Section on Brute Force
- as CP4 says, you can precompute anwers
"""
from itertools import product

for _ in range(int(input())):
    n = int(input())
    
    res = {}
    OPS = ['*','+','-','//']
    
    for p in product(OPS, repeat = 3):
        expr = "4 {} 4 {} 4 {} 4".format(*p)
        tmp = eval(expr)
        if tmp not in res:
            res[tmp] = (expr + " = {}".format(tmp)).replace('//','/')
    
    print(res.get(n, "no solution"))