# Cinema Crowds 2
# https://open.kattis.com/problems/cinema2
# TAGS: basic, array
# CP4: 1.4e, Control Flow
# NOTES:
N, M = map(int, input().split())

xs = map(int, input().split())

acc = 0
cnt = 0

for x in xs:
    if acc + x <= N:
        acc += x
        cnt += 1
    else:
        break

print(M - cnt)