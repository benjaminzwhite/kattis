# Dominoes 2
# https://open.kattis.com/problems/dominoes2
# TAGS: graph
# CP4: 4.2h, Really Ad Hoc
# NOTES:
"""
Confusing input format; got WA for 2 submits - you are supposed to print TOTAL NUMBER OF DOMINOES *AFTER ALL DOMINOES* PUSHED,

I thought (and the first 2 testcases pass with this interpretation) that you print after each domino in the l list/queries -> multiple testcases etc

So basically I had res=0 and seen = [0]*n WITHIN the l loop but in fact you need it outside and only print 1 number res for each of the T testcases
"""
from collections import defaultdict

T = int(input())
for _ in range(T):
    n, m, l = map(int, input().split())

    d = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        d[u].append(v)
    # dfs
    res = 0
    seen = [0] * (n + 5)
    for _ in range(l):
        z = int(input())
        stk = [z]
        #seen = [0] * (n+5) # this is where error was, i had res=0 inside each loop BUT IT WANTS OVERALL TO UPDATE FOR EACH TESTCASE, NOT EACH l
        while stk:
            curr = stk.pop()
            if seen[curr]:
                continue
            res += 1
            seen[curr] = 1
            for adj_v in d[curr]:
                stk.append(adj_v)
    print(res)