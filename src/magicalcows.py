# Magical Cows
# https://open.kattis.com/problems/magicalcows
# TAGS: dict
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Pet peeve of mine:

I was getting WA on first submits, so I guessed maybe the inputs aren't always sorted - indeed this is the reason why I was getting WA -.-

I find it really annoying when exercises do this, as a kind of "gotcha", especially when the given testcases all show sorted inputs:
it doesn't add anything to the exercise.
(or maybe this is a cultural difference with other OJs, where "sample testcases should be representative").
"""
from math import floor, ceil

C, N, M = map(int, input().split())

d = {}
for i in range(N):
    c_i = int(input())
    d[c_i] = 1 + d.get(c_i, 0)

RES = [sum(d.values())]

for _ in range(50):
    d_ = {}
    for k, v in d.items():
        k_ = 2 * k
        if k_ > C:
            tmp1 = ceil(k_ / 2)
            tmp2 = floor(k_ / 2)
            d_[tmp1] = v + d_.get(tmp1, 0)
            d_[tmp2] = v + d_.get(tmp2, 0)
        else:
            d_[k_] = v + d_.get(k_, 0)
    d = d_
    RES.append(sum(d.values()))

for _ in range(M):
    day = int(input())
    print(RES[day])