# Knot Knowledge
# https://open.kattis.com/problems/knotknowledge
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Below approach is very inefficient, was checking to see if slow approaches are AC since n <= 50
"""
n = int(input())

xs = input().split()
ys = input().split()

print(next(x for x in xs if x not in ys))