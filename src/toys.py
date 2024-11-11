# Toys
# https://open.kattis.com/problems/toys
# TAGS: simulation
# CP4: 3.2j, Josephus Problem
# NOTES:
"""
Classic Josephus - reread:
https://cp-algorithms.com/others/josephus_problem.html
"""
T, K = map(int,input().split())

j = 0
for n in range(1, T + 1):
    j = (j + K) % n

print(j)