# Fenwick Tree
# https://open.kattis.com/problems/fenwick
# TAGS: fenwick tree, interpreter, improve
# CP4: 2.4c, Tree-related DS
# NOTES:
"""
I got a few TLE for first submit: I thought it was a bug/error due to my implementation
e.g. LSOne(0) causing infinite loop, which is a common Fenwick tree error (see Halim CP4 book discussion)

-> but in fact, no, it's just due to the INPUT/reading the test cases because they are so large.

So, in Python at least, you need to use some stdin functions rather than just input() to read the testcases etc.

---

TODO: IMPROVE: My solution below still takes 3.7 seconds, maybe can improve with faster input or something?
"""
def LSOne(n):
    """
    returns value of least significant set bit of n 

    example: LSOne(90) = LSOne(10110|1|0) = 2**1 = 2
    """
    return n & (-n)


class FenwickTree():

    def __init__(self, m):
        # m keys
        self.ft = [0] * (m + 1) # creates the empty Fenwick array

    def rsq_to_right(self, j):
        res = 0
        while j > 0:
            res += self.ft[j]
            j -= LSOne(j)
        return res

    def rsq(self, i, j):
        return self.rsq_to_right(j) - self.rsq_to_right(i - 1)

    def update(self, i, val):
        # updates value of the i'th element of the fenwick array ft[] by val
        # NOTE: val can be positive or negative
        M = len(self.ft)
        while i < M:
            self.ft[i] += val
            i += LSOne(i)


# --- Exercise starts here ---
from sys import stdin, stdout

N, Q = [int(x) for x in stdin.readline().split(' ')]

FT = FenwickTree(N)

for _ in range(Q):
    op, *vals = stdin.readline().split(' ')
    if op == '+':
        i, val = map(int, vals)
        FT.update(i + 1, val)
    else:
        i = int(vals[0])
        print(FT.rsq_to_right(i))