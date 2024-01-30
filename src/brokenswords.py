# Broken Swords
# https://open.kattis.com/problems/brokenswords
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
N = int(input())

TB, LR = 0, 0

for _ in range(N):
    s = input()
    TB += s[:2].count('0')
    LR += s[2:].count('0')

res = min(TB, LR) // 2

print(res, TB - 2 * res, LR - 2 * res)