# Zapis
# https://open.kattis.com/problems/zapis
# TAGS: dynamic programming, mathematics, combinatorics, improve
# CP4: 6.3b, DP String, Non Classic
# NOTES:
"""
TODO: IMPROVE:

I got WA on first submissions after 8-9 testcases - I was trying to solve "last 5 digits" requirement with mod 100_000, but I'm guessing
it wants you to handle leading 0's ??? For example, if answer is 04795 it wants this, rather than 4795?
In any case I "solved" this issue quickly by abusing Python bigint, I just compute FULL HUGE ANSWER (lol), convert res to string,
and print str(res)[-5:] at the end (very Pythonic O_o)

---

TODO: IMPROVE: I'm sure there's a simple way with inclusion exclusion to get the answer (answer for ??... is going to be 3**n * Catalan(n))

---

TODO: IMPROVE: practice implement the bottom up dynamic programming version

---

Main comments are in code below.

It's dynamic programming with some combinatorics: kept illustration to understand the recursive breakdown of the string:

    i=0 MUST BE AN OPENING BRACKET (same for all recursive substrings' first char)
     V
 i = 0 1 2 3 4 5 6 7 8 9     
 s = [ ? ? ] ? ( ? ? ? ?

     S ^-^ E ^---------^    <<<=== then recurse on these 2 substrings [1:2], [5:9], and consider whether S+E is a valid pairing
            |
            |  <--- this dividing line is an example of what i'm calling "close" in below, you can range it over all ODD INDICES
"""
from functools import lru_cache

MATCHING_LOOKUP = { 
      ('?', '?'):3,
      ('[', '?'):1,
      ('(', '?'):1,
      ('{', '?'):1,
      ('?', ']'):1,
      ('?', ')'):1,
      ('?', '}'):1,
      ('[', ']'):1,
      ('(', ')'):1,
      ('{', '}'):1,
      }

BIGMOD = 100_000 # exercise asks for last 5 digits only

@lru_cache(maxsize=None)
def solve(start, end):
    # base case: when start > end for the current recursive string call, you have no more subproblems to solve
    if start > end:
        return 1

    cnt = 0
    # 1) try to form a matching pair with curr start char, s[start], by considering all viable close positions ahead of this start, and up to the end
    # -> close position is viable if it is ODD INDEXED since first char must be an OPENING bracket
    # -> if the s[start], s[close] pair is viable, you will get a combinatorial multiplication of either:
    #    1 (if either of the chars is "specified" since then other char is fixed)
    #    3 (if both chars are free: '?')
    #    0 (if both chars mismatch, since this string is not a valid option)
    # 2) form the corresponding "inside prefix" leftover (i.e. the string inside the current "outer" s[start], s[close])
    # 3) form the corresponding "suffix" leftover (i.e. the string from s[close]+1 to the s[end])
    # -> Recurse/combinatorially multiply the contributions from 1,2,3 and sum them to total cnt
    for close in range(start + 1, end + 1, 2):
        curr_pair = (s[start], s[close])
        curr_pair_cnt = MATCHING_LOOKUP.get(curr_pair, 0) # 0 if pair is not valid ie not in LOOKUP

        inside_prefix_cnt = solve(start + 1, close - 1)
        suffix_cnt = solve(close + 1, end)

        cnt += (curr_pair_cnt * inside_prefix_cnt * suffix_cnt) # should take % BIGMOD

    return cnt # should take % BIGMOD

N = int(input())
s = input()

res = solve(0, N - 1)

print(str(res)[-5:]) # TODO: IMPROVE: lazy implementation of last 5 digits requirement O_o