# Powers and Modulus
# https://open.kattis.com/problems/powers
# TAGS: mathematics, number theory, nice
# CP4: 5.8a, Matrix Power
# NOTES:
"""
Nice exercise, I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/powers.md
"""
a, b = map(int, input().split())

res = pow(a // 2, b, a) if a % 2 == 0 else 0

print(res)