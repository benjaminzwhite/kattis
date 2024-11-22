# Frosh Week
# https://open.kattis.com/problems/froshweek2
# TAGS: greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
n, m = map(int, input().split())

ts = list(map(int, input().split()))
ls = list(map(int, input().split()))

ts = sorted(ts)
ls = sorted(ls)

i_t, i_l = 0, 0
res = 0

curr = 0
while i_t < len(ts) and i_l < len(ls):
    if curr + ts[i_t] <= ls[i_l]:
        curr += ts[i_t]
        i_t += 1
        res += 1
    else:
        curr = 0
        i_l += 1

print(res)