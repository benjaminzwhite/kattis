# Entering the Time
# https://open.kattis.com/problems/enteringthetime
# TAGS: BFS
# CP4: 8.2c, State-Space, BFS, H
# NOTES:
"""
It is standard BFS, but made "difficult" by the fact that the explanations are confusing:

Originally I had for [custom testcase while debugging:]
e.g. start = 00:53 end = 23:01 the following result, where you "push the 5 over into 6->0 rollover"

00:53
10:53
20:53
21:53
22:53
23:53
23:03
23:02
23:01

but the expected result [see comments in code below where I adjusted the "rollover" conditons for minutes m1] is somehow to NOT ALLOW THIS:
instead the expected result (based on my AC solution) for above testcase would be:

00:53
10:53
20:53
21:53
22:53
23:53
23:43
23:33
23:23
23:13
23:03
23:02
23:01

which requires 13 steps instead of 9.

It's not clear from the instructions why the first solution is not allowed? The only explanation I can think of - but again this is not stated
in the problem statement - is that going from 23:53 -> 23:03 by "increasing the 5 to reach "5+1 = 6" i.e. == 0" is not allowed because somehow the
hours are coupled to the minutes digits? So he is implying that it would toggle the 23h to 24h or something like that??? I mean the "next digit"
when you increase from 5 in that column should indeed be 0 ? That column/position can never contain a 6 ???

As seen in the code below, by modifying my logic, in order to get AC we need to allow the m1 minute position (i.e this one _ _ : m1 _ ) to reach 9????
I thought 5 would be the correct max digit value here?????
"""
from collections import deque

s = input()
e = input()

start = list(int(s[i]) for i in [0, 1, 3, 4])
end = list(int(e[i]) for i in [0, 1, 3, 4])

seen = set()
q = deque([(start, [start])])
while q:
    curr, sol = q.popleft()
    val = sum(x * 10**exp for x, exp in zip(curr, range(3, -1, -1))) # just some way to have a hashable item to lookup in seen()
    
    if curr == end:
        res = sol
        break
    
    if val in seen:
        continue

    seen.add(val)

    for pos in range(4): # not very DRY - was doing this full typing out cases because of debugging unclear problem statement
        for move in (-1, 1):
            tmp = curr[:]
            tmp[pos] += move
            h1, h2, m1, m2 = tmp
            if m2 < 0:
                tmp[3] = 9
            if m2 == 10:
                tmp[3] = 0
            if m1 < 0:
                tmp[2] = 9 # instead of 9, this value used to be 5 - really unclear explanation if this is what is wrong
            if m1 == 10: # instead of 10 this used to be 6
                tmp[2] = 0
            if h2 == 10:
                tmp[1] = 0
            if h2 < 0:
                tmp[1] = 9
            if 0 <= 10 * tmp[0] + tmp[1] < 24 and 0 <= 10 * tmp[2] + tmp[3] < 60:
                q.append((tmp, sol[:] + [tmp]))

print(len(res))
for h1, h2, m1, m2 in res:
    print(f"{h1}{h2}:{m1}{m2}")