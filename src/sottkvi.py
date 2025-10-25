# Sóttkví
# https://open.kattis.com/problems/sottkvi
# TAGS: basic
# CP4: 1.4h, Control Flow, Level 2
# NOTES:
n, k, d = map(int, input().split())

target = d + k
res = 0
for _ in range(n):
    x = int(input())
    if x + 14 <= target:
        res += 1

print(res)