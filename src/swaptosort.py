# Swap to Sort
# https://open.kattis.com/problems/swaptosort
# TAGS: union find
# CP4: 2.4b, Union-Find
# NOTES:
"""
Nice exercise - just think about it a bit:

The pairs e.g. (1,3) (1,4) (4,3) determine which elements can be "reached" and in the final sorted state you
want to go from N,...3,2,1 to -> 1,2,3...N
which means that N needs to be in same "cycle" as 1, N-1 in same cycle as 2 etc.

So just add all the pairs to union find
-> put all elements that can be swapped into the same set
-> then at end, for each element i=1,2,...N check that N-i+1 is in the same set as i.

---

Note: my implementation of Union Find here doesn't do the path compression speed-up from Halim CP4 book
"""
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
N, K = map(int, input().split())

uf = UnionFind(N + 1)

for _ in range(K):
    fst, snd = map(int, input().split())
    uf.union_set(fst, snd)

flg = True
for i in range(1, N + 1):
    if not uf.is_same_set(i, N - i + 1):
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")