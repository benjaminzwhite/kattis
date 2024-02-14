# Planetaris
# https://open.kattis.com/problems/planetaris
# TAGS: greedy, sorting
# CP4: 3.4b, Involving Sorting, E
# NOTES:
n, a = map(int, input().split())

xs = sorted(map(int, input().split()))

cnt = 0
i = 0
while i < len(xs):
    curr = xs[i]
    if a >= curr + 1:
        a -= curr + 1
        i += 1
        cnt += 1
    else:
        break

print(cnt)