# Union-Find
# https://open.kattis.com/problems/unionfind
# TAGS: union find, interpreter, improve
# CP4: 2.4b, Union-Find
# NOTES:
"""
This problem (AFAICT, unless I missed a simpler way of solving) requires you to implement the path compression technique
to speed up the UnionFind class if you want to pass the time limit in Python (1 second).

I left notes in code below with the "old" and "new" implementations inside the main class, to show how the path compression
works here.

---

TODO: IMPROVE: my solution still takes 0.8 seconds in Python, there must be some more optimizations to make it go faster?
(I already saw that I get TLE if I use input() for reading in testcases, so I'm using stdin here to workaround that slowness)

Maybe you can avoid building the children[] list, and just do a single pass by updating "self.parents[c] = parent_i" as you go?

Or you're supposed to solve in C++ rather than Python?
"""
class UnionFind():

    def __init__(self, N):
        self.parents = list(range(N))
        self.rank = [0 for _ in range(N)]
        self.set_size = [1 for _ in range(N)]
        self.num_sets = N

    # CARE!
    # this is the OLD find_set **WITHOUT** path compression trick
    def find_set_no_path_compression(self, i):
        if self.parents[i] == i:
            return i
        else:
            return self.find_set_no_path_compression(self.parents[i])

    # based on the code of CP4 Halim book, after studying why the path compression leads to speedup:
    # see:
    # https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/unionfind_ds.py
    def find_set(self, i):
        parent_i = i
        children = []
        while parent_i != self.parents[parent_i]:
            children.append(parent_i)
            parent_i = self.parents[parent_i]
        # this is the path compression bit, speeds up future queries
        for c in children:
            self.parents[c] = parent_i
        return parent_i

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def num_disjoint_sets(self):
        return self.num_sets

    def size_of_single_set(self, i):
        return self.set_size[self.find_set(i)]

    def union_set(self, i, j):
        if self.is_same_set(i, j):
            return
        else:
            r_i = self.find_set(i)
            r_j = self.find_set(j)
            if self.rank[r_i] > self.rank[r_j]:
                r_i, r_j = r_j, r_i
            self.parents[r_i] = r_j
            if self.rank[r_i] == self.rank[r_j]:
                self.rank[r_j] += 1
            self.set_size[r_j] += self.set_size[r_i]
            # ------
            # UPDATE TO MY UNIONFIND IMPLEMENTATION:
            self.set_size[r_i] = 0 # TBC CHECK THIS WORKS: I added it myself as a way to track the actual set sizes
            # ------
            self.num_sets -= 1


# --- Exercise starts here ---
from sys import stdin

N, Q = map(int, stdin.readline().split())

uf = UnionFind(N)

for _ in range(Q):
    op, a, b = stdin.readline().split()
    a = int(a)
    b = int(b)
    if op == '=':
        uf.union_set(a, b)
    else:
        if uf.is_same_set(a, b):
            print("yes")
        else:
            print("no")