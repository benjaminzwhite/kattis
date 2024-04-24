# Limbo: Part 1
# https://open.kattis.com/problems/limbo1
# TAGS: mathematics
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
A bit overranked O_o just express in terms of triangular numbers
"""
T = int(input())

for _ in range(T):
    l, r = map(int, input().split())

    n = 1 + l + r
    row_triangular_number = n * (n + 1) // 2 # the triangular number at the rightmost position in the n'th row
    offset = l

    print(row_triangular_number - offset)