# Divvying Up
# https://open.kattis.com/problems/divvyingup
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
n = int(input())

W = map(int, input().split())

if sum(W) % 3 == 0:
    print("yes")
else:
    print("no")