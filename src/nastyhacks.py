# Nasty Hacks
# https://open.kattis.com/problems/nastyhacks
# TAGS: basic
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())
    x = e - c
    if x > r:
        print("advertise")
    elif x == r:
        print("does not matter")
    else:
        print("do not advertise")