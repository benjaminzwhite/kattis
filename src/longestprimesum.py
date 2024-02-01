# Longest Prime Sum
# https://open.kattis.com/problems/longestprimesum
# TAGS: basic, mathematics
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
Answer is either 2+2+2+2 or 2+2+2+3 ... depending on n even or odd.
Res is always n//2 terms though
"""
n = int(input())

res = n // 2

print(res)