# Eeny Meeny
# https://open.kattis.com/problems/eenymeeny
# TAGS: simulation
# CP4: 3.2j, Josephus Problem
# NOTES:
from itertools import cycle

message = input()
n_kids = int(input())
kids = [input() for _ in range(n_kids)]

jumps = len(message.split())
seen = set()
res = []
it = cycle(range(n_kids))

for _ in range(n_kids):
    j = jumps
    while j > 0:
        i = next(it)
        if i not in seen:
            j -= 1
    curr = kids[i]
    seen.add(i)
    res.append(curr)

print((len(res) + 1) // 2) # first team is always biggest so regardless of odd/even res size, this will print ceil(n/2) e.g. 5-> 3 team A, 2 team B
for name in res[::2]:  # print the 0th,2nd,4th members of res-> they are the ones who were added to team A on turn 0,2,4,....
    print(name)
print(len(res) // 2)
for name in res[1::2]: # print the 1st,3r,5th members of res-> they are the ones who were added to team B on turn 1,3,5....
    print(name)