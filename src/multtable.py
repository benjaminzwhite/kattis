# Multiplication Table
# https://open.kattis.com/problems/multtable
# TAGS: mathematics, number theory
# CP4: 0, Not In List Yet
# NOTES:
N, M = map(int, input().split())

RANGE_MAX = min(N, int(M**0.5))

cnt = 0
for d in range(1, RANGE_MAX + 1):
    if M % d == 0:
        if M // d == d:
            cnt += 1
        elif M // d <= N:
            cnt += 2

print(cnt)