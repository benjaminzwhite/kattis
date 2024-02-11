# Field Trip
# https://open.kattis.com/problems/fieldtrip
# TAGS: array
# CP4: 3.5a, Max 1D/2D Range Sum
# NOTES:
"""
There's a much shorter way to solve, if you want to code golf this. Below is explanation for current approach:

Since it was ranked low easy/green I tried brute force over i and j and sum(xs[:i]) == sum(xs[i:j]) == sum(xs[j:]) etc
That timed out so tried with accumulate and check acc[i] == (acc[j] - acc[i]) == (acc[-1] - acc[j]) that ALSO times out.

So you have to actually do a quite sophisticated check:

The total sum of the student groups must be divisible by 3
-> get S from accumulate, it is the acc[-1] value (sum of all xs)
-> check that S%3 == 0, if not then solution is impossible, can never divide the students into 3 groups to fit on buses exactly
Then
a) iterate through the accumulate list and search for the first time you hit the exact needed bus_size = S//3, store that index
b) from that index from a), now search for bus_size + bus_size = 2*bus_size , which represents needing to accumulate the 2nd new bus with exactly S//3 students
If you reach that target in accumulate, then the indices i, i+j are the answers, else there is no solution.

CARE! Lots of i+1 / j+1 type confusion possible due to indexing choices etc.
"""
from itertools import accumulate

N = int(input())

xs = map(int, input().split())

acc = list(accumulate(xs))

S = acc[-1]

if S % 3 != 0:
    print(-1)
else:
    bus_size = S // 3
    flg1 = False
    i1 = 0
    for i, x in enumerate(acc):
        if x == bus_size:
            i1 = i
            flg1 = True
            break
    if flg1:
        flg2 = False
        j1 = 0
        for j, y in enumerate(acc[i:]): # CARE! continue from index i = i1 for second part of the checking requirement
            if y == bus_size * 2:
                j1 = j
                flg2 = True
                break
    if flg1 and flg2:
        print(i1 + 1, i1 + j1 + 1) # NB not j1+1 since we enumerated(acc[i:]) from 0 -> more elegant to enumerate(acc[i:], i1) <-- using the result i1 here
    else:
        print(-1)