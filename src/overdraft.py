# Overdraft
# https://open.kattis.com/problems/overdraft
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
n = int(input())

acc = 0
res = 0

for _ in range(n):
    acc += int(input())
    res = min(res, acc)

print(-res)