# Batter Up
# https://open.kattis.com/problems/batterup
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
n = int(input())

xs = map(int, input().split())

bases, cnt = 0, 0

for x in xs:
    if x >= 0:
        cnt += 1
        bases += x

print(bases / cnt)