# Putovanje
# https://open.kattis.com/problems/putovanje
# TAGS: array, brute force
# CP4: 9.slid, Sliding Window
# NOTES:
"""
Compute all possible sums for LHS and RHS of a given position, k, and find best result

Do it intelligently though to avoid recomputing all the terms:

start with 0 numbers in the lhs, and all the numbers in rhs (so rhs = sum(xs))

then for each value x moving from left to right, you:
+ increment the current lhs total by x**2
- decrememt the current rhs total by x

"""
n = int(input())

xs = []
lhs = 0
rhs = 0
best = 0

for _ in range(n):
    x = int(input())
    rhs += x
    xs.append(x)
    
for x in xs:
    lhs += x * x
    rhs -= x
    best = max(best, lhs * rhs)
    
print(best)