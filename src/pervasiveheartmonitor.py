# Pervasive Heart Monitor
# https://open.kattis.com/problems/pervasiveheartmonitor
# TAGS: basic
# CP4: 1.6m, Input Parsing (Iter)
# NOTES:
from sys import stdin

for line in stdin:
    name = []
    total, cnt = 0, 0
    for x in line.split():
        if x.isalpha():
            name.append(x)
        else:
            total += float(x)
            cnt += 1
    print(f"{total / cnt} {' '.join(name)}")