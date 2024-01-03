# Chanukah Challenge
# https://open.kattis.com/problems/chanukah
# TAGS: basic
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
- Gauss schoolboy formula
"""
n = int(input())

for _ in range(n):
    i, m = map(int, input().split())
    print(f"{i} {m + m*(m+1)//2}")