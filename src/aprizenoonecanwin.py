# A Prize No One Can Win
# https://open.kattis.com/problems/aprizenoonecanwin
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
n, X = map(int, input().split())

xs = sorted(map(int, input().split()))

prev = xs[0]
cnt = 1
for x in xs[1:]:
    if x + prev <= X:
        cnt += 1
    else:
        break
    prev = x

print(cnt)