# Bridges and Tunnels
# https://open.kattis.com/problems/bridgesandtunnels
# TAGS: union find, improve
# CP4: 2.4b, Union-Find
# NOTES:
"""
TODO: IMPROVE: my solution runs slow because this does not implement the "path compression" optimization for Union Find

---

Weird input format - it tells you how many bridges there are BUT NOT HOW MANY BUILDINGS ?

Does this mean, since number of bridges is at most 100_000 = N*(N-1)//2 (???), you can conclude that

N <= sqrt(200_000) ~ 450ish ???

(This is needed because you need to assign the BUILDING (strings/words) to indices in the UnionFind array.)

---

UPDATE: I got error when putting 450 or 500 even? I really don't understand the input/problem statement.

Maybe they mean that if there are at most 100_000 bridges, there are at most 2 * 100_000 buildings???

I just put 200_000 as max limit and I got AC, so it seems to work.
"""
# based on the C++ version in Halim CP4 book
class UnionFind():

    def __init__(self, N):
        self.parents = list(range(N))
        self.rank = [0 for _ in range(N)]
        self.set_size = [1 for _ in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.parents[i] == i:
            return i
        else:
            return self.find_set(self.parents[i])

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
            self.num_sets -= 1

# --- Exercise starts here ---
n = int(input())

# I got RTE when use 500 so I just use a huge number
# I'm assuming then that max number of buildings is 2 * 100_000 ?? (or 2*n in general)
uf = UnionFind(200500)
d = {}
curr_id = 0

for _ in range(n):
    a, b = input().split()
    
    if a not in d:
        d[a] = curr_id
        curr_id += 1
    
    if b not in d:
        d[b] = curr_id
        curr_id += 1
    
    a_ = d[a]
    b_ = d[b]
    uf.union_set(a_, b_)
    
    print(uf.size_of_single_set(a_))