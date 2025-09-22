# Association for Control Over Minds
# https://open.kattis.com/problems/control
# TAGS: union find, improve
# CP4: 2.4b, Union-Find
# NOTES:
"""
TODO: IMPROVE: I don't yet implement the path compression trick described in Halim CP4 book to speedup union find.

---

Reading comprehension:

Basically you want to track the REPRESENTATIVES of each INGREDIENT needed for the current recipe, add those representatives
to a set (for each separate recipe) so that they are only counted once, then count how many ingredients are in that
representative's current set (which you can find via the UnionFind.size_of_single_set)

-> if you can account for all M ingredients for the current recipe, then you can make it OK
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
N = int(input())

# CARE! Don't confuse N rather than M here.
# Reading comprehension: N recipes M ingredients or w/e it is
M_MAX = 500_123
uf = UnionFind(M_MAX)

res = 0
for _ in range(N):
    M, *xs = map(int, input().split())

    # this ends up corresponding to "CAULDRONS"
    # i.e. suppose 1,3,4 have same set_repr (say '3' WLOG)
    # then -> 1,3,4 are in same cauldron '3' together
    set_representatives = set()

    for x in xs:
        set_representatives.add(uf.find_set(x))

    #print(set_representatives)
    num_ingredients = 0
    for representative in set_representatives:
        num_ingredients += uf.size_of_single_set(representative)

    if num_ingredients == M:
        #print("DEBUG: OK CAN MAKE: ", xs)
        res += 1
        
        # merge the sets if this potion got made:
        # -> do the UNION step of the cauldrons => all one big cauldron now
        tmp = set_representatives.pop() # <- here I pop() to get an arbitrary first value to "start" the union_set with
        for x in set_representatives:
            uf.union_set(tmp, x)

print(res)