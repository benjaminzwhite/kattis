# License to Launch
# https://open.kattis.com/problems/licensetolaunch
# TAGS: basic
# CP4: 1.4e1, Control Flow, Easy
# NOTES:
n = int(input())

xs = map(int, input().split())

min_junk = float('inf')
res = 0

for i, x in enumerate(xs):
    if x < min_junk:
        min_junk = x
        res = i

print(res)