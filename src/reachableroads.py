# Reachable Roads
# https://open.kattis.com/problems/reachableroads
# TAGS: graph, union find
# CP4: 4.2a, Finding CCs
# NOTES:
class UnionFind():

    def __init__(self, N):
        self.parents = list(range(N))
        self.rank = [0 for _ in range(N)]
        self.set_size = [1 for _ in range(N)]
        self.num_sets = N

    # based on the code of CP4 Halim book, after studying why the path compression leads to speedup:
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
        if self.is_same_set(i,j):
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
            # update to store/track actual set size
            self.set_size[r_i] = 0
            # ------
            self.num_sets -= 1

# --- Queries ---
T = int(input())
for _ in range(T):
    N = int(input())
    uf = UnionFind(N)
    
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        uf.union_set(u, v)
    
    print(uf.num_disjoint_sets() - 1) # CARE! -1 as that's how many CONNECTIONS between the disjoint sets you need to add to merge them
    