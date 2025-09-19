# Virtual Friends
# https://open.kattis.com/problems/virtualfriends
# TAGS: union find
# CP4: 2.4b, Union-Find
# NOTES:
"""
Seems to be very similar to:

https://open.kattis.com/problems/bridgesandtunnels
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
T = int(input())
for _ in range(T):
    F = int(input())
    
    uf = UnionFind(F + 1)
    d = {}
    curr_id = 0
    for _ in range(F):
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