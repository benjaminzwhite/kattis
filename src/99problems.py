# 99 Problems
# https://open.kattis.com/problems/99problems
# TAGS: mathematics, number theory
# CP4: 3.2g, Try All Answers
# NOTES:
"""
Don't need to brute force, can solve analytically
"""
n = int(input())

q, r = divmod(n, 100)

if q == 0:
    print(99)
elif r < 49:
    print((q - 1) * 100 + 99)
else:
    print(q * 100 + 99)