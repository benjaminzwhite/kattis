# Cold-puter Science
# https://open.kattis.com/problems/cold
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
n = int(input())

xs = map(int, input().split())

res = sum(x < 0 for x in xs)

print(res)