# Out of Sorts
# https://open.kattis.com/problems/outofsorts
# TAGS: binary search
# CP4: 3.3a, Binary Search
# NOTES:
"""
Long description - basically question is:

1. Generate a somewhat disordered list of integers (using some % formula, details don't matter exactly)

2. Now, for each of the values that appear in that sequence, can you find that value within the sequence if you use standard binary search?

nb. the array is NOT sorted, you just "pretend" that you are binary searching with l,r indices.
Sometimes you will land on a target value eventually, sometimes not.

e.g. [1000,5,3] <- here if target is 1000, first binary search index is 0+2//2 =1 which has value 5 < 1000
-> so you binary search on RIGHT HALF, but of course you won't find 1000 now
"""
n, m, a, c, xzero = map(int, input().split())

# CARE! reading description the original xzero is NOT considered part of the sequence O_o
# NOTE: DO NOT ADD XZERO TO SEQUENCE -.- SO DO 1 STEP MANUALLY TO SEED SEQUENCE then n-1 <--!!! not n, manually referring to seq[-1] element
xone = (a * xzero + c) % m 
sequence = [xone]

# n-1 !!! see note above
for _ in range(n - 1):
    x = (a * sequence[-1] + c) % m
    sequence.append(x)

seen = set()

for target in sequence:
    l, r = 0, len(sequence) - 1
    while l <= r:
        mid = (l + r) // 2
        curr = sequence[mid]
        if curr == target:
            seen.add(curr)
            break
        elif curr > target:
            r = mid - 1
        else:
            l = mid + 1

print(len(seen))