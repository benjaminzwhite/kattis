# Coffee Cup Combo
# https://open.kattis.com/problems/coffeecupcombo
# TAGS: greedy
# CP4: 1.4g, 1D Array, Easier
# NOTES:
n = int(input())
s = input()

cnt = 0
cups = 0

for c in s:
    if c == '1':
        cups = 2
        cnt += 1
    else:
        if cups > 0:
            cnt += 1
        cups = max(0, cups - 1)

print(cnt)