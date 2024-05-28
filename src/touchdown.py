# Touchdown!
# https://open.kattis.com/problems/touchdown
# TAGS: interpreter
# CP4: 1.6p, Time Waster, Harder
# NOTES:
"""
Reading comprehension - helps to understand the rules of American football O_o

First submission WA because I wasn't returning Nothing when e.g. reach end of xs and no events have triggered (specifically, when plays <4)

e.g. testcase "2 3 2" would NOT print anything in my first submission
-> So I use flg=1 as default so if reach end of xs, will print flg=1 case
"""
N = int(input())
xs = list(map(int, input().split()))

distance = 20
curr_advance = 0
plays = 0
flg = 1
for x in xs:
    if plays == 4:
        flg = 1
        break
    plays += 1
    curr_advance += x
    if curr_advance >= 10:
        plays = 0
        curr_advance = 0
    distance += x
    if distance >= 100:
            flg = 2
            break
    if distance <= 0:
        flg = 3
        break

if flg == 1:
    print("Nothing")
elif flg == 2:
    print("Touchdown")
else:
    print("Safety")