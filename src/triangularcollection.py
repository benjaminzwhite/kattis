# Triangular Collection
# https://open.kattis.com/problems/triangularcollection
# TAGS: mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
You can label groups of the multisets with the desired property according to the lowest + highest element in the multiset.

Then add to the label the 2nd lowest element in the multiset (you now have 3 elements which is the minimum required of course)

Now, **any element that is > 2nd lowest and < highest** can be included/not included under this fundamental labelling; since by 
ordering it will always satisfy

lo + middle' >= lo + middle_original > highest

and also satisfy

middle' + middle_original >= lo + middle_original > highest

(these are the 2 extreme cases, so all other triples of integers will define a triangle also)

-> so just iterate (n=50) over all candidates for lowest + highest element
-> then within that range, try all possible "middle" elements.
=> then combinatorially, the number of values satisfying middle < v < hi, will give you all 2**v possible subsets to include, or not,
with the "fundamental starting multiset" {lo, middle, hi} being included (which corresponds to not picking any of the v's in this interval)

Quick check: note that if middle has idx i and hi has idx i+1 then this range has 0 v-elements, so will generate 2**0 = 1 subset: {lo, middle, hi}

---

Implementation note:

Of course you need to sort the xs, for the ordering requirement above, since input isn't sorted!
"""
n = int(input())
xs = []
for _ in range(n):
    xs.append(int(input()))

xs = sorted(xs)

res = 0
for hi in range(n):
    for low in range(hi):
        for middle in range(low + 1, hi):
            if xs[low] + xs[middle] > xs[hi]:
                res += 2 ** (hi - middle - 1)

print(res)