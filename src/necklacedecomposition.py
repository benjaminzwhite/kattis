# Shortest Composite Sum
# https://open.kattis.com/problems/shortestcompositesum
# TAGS: greedy, string, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
Nice little exercise - easier than it sounds if you read exercise statement carefully:

Since it tells you decomposition is UNIQUE you know a greedy approach must work:
- greedy try to build largest possible prefix that is itself a necklace
- now you have a prefix which is a necklace, and a leftover string which by assumption also has a unique decomposition
=> do this until have covered all the elements in the string from left to right.

Implementation note:

TODO: review this, not 100% sure why it's happening O_o

I tried resubmitting exact same solution WITHOUT CACHING the is_valid_necklace() and it passes (even seems faster lol)
"""
from functools import lru_cache

# There are up to 250 testcases:
# I generated locally 250 random strings of 1 & 0 and get thousands of CacheInfo(hits) so seems worth caching this function
@lru_cache(maxsize=None)
def is_valid_necklace(T_candidate):
    # note: was getting errors -> have to check that the shifted candidate pattern != s since otherwise '111' will NOT count as a necklace
    # i.e. '111' < '111' is FALSE so the all() comprehension will return FALSE for s = '111' when in fact it should be TRUE
    return all(shifted > T_candidate for j in range(len(T_candidate)) if (shifted := (T_candidate[j:] + T_candidate[:j])) != T_candidate)

n = int(input())
for _ in range(n):
    S = input()
     
    i = 0
    L = len(S)
    res = []
    while i < L:
        # exercise statement means you can cheese it; since it tells you decomposition is unique you know a greedy approach will work:
        # greedy try to build largest possible prefix that is itself a necklace; now you have a prefix which is a necklace, and a leftover
        # string which by assumption also has a unique decomposition -> do this until have covered all the elements in the string from left to right.
        for T_size in range(L - i, 0, -1):
            T_candidate = S[i:i + T_size]
            if is_valid_necklace(T_candidate):
                res.append(f"({T_candidate})") # CARE! note formatting/output requirement like (111)(01111)(011)
                i += T_size - 1 # !!! I will +1 after break statement to get the +1 to the i index in all cases as part of the while loop
                break
        i += 1
    print(''.join(res))