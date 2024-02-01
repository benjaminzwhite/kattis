# Cinema Crowds
# https://open.kattis.com/problems/cinema
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
N, M = map(int, input().split())

res = 0

xs = map(int, input().split())

for x in xs:
    if x <= N:
        N -= x
    else:
        res += 1

print(res)