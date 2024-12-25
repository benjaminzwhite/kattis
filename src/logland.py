# Logland
# https://open.kattis.com/problems/logland
# TAGS: binary, logic, proof
# CP4: 3.4f, Non Classical, Harder
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/logland.md
"""
BIGMOD = 10**9 + 7

N = int(input())
xs = list(map(int, input().split()))

res = 0
glued_coins = 0
for exp, real_coins in enumerate(xs):
    if (real_coins % 2 == 1) and (glued_coins == 0):
        res += pow(2, exp, BIGMOD)
    glued_coins = (glued_coins + real_coins) // 2

print(res % BIGMOD)