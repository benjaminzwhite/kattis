# Mountain Scenes
# https://open.kattis.com/problems/scenes
# TAGS: mathematics, combinatorics, proof, dynamic programming, improve
# CP4: 4.6b, Counting Paths, Easier
# NOTES:
"""
TODO: IMPROVE:

I first did a dynamic programming solution, but it seems to need to be an efficient implementation in Python otherwise is too slow
I didn't see how to optimise the dp approach quickly so solved analytically instead - will return to make a Python dp solution

---

Combinatorics proof:

You can convert this exercise into the following combinatorics one:
-assume (for now) you have a fixed amount of ribbon R
-the width is w and height is h

"How many integer solutions are there to x_1 + x_2 + x_3 +...+ x_w == R such that ALL x_i <= h"

The answer is inclusion exclusion on solutions which have 1, 2, 3... w of the x's with values > h:

Choose i bad columns in comb(w,i) ways, give them h+1 "cubes" (or whatever) each, then assign the remaining R - i * (h+1) cubes freely with replacement
amongst all the w columns.

By PIE the number of solutions which have NO bad columns is:

total - 1 bad col + 2 bad col ...
= sigma_all_values_of_i( pow(-1,i) * comb(w,i) * comb_with_replacement(w, R - i*(h+1)))

This is for one exact value of R -> to get the answer to the exercise, we calculate this quantity FOR ALL POSSIBLE VALUES OF R: R = 0,1,2,...n inclusive.

Finally small adjustment; we are told to ignore solutions which have all heights the same: this is easy to 
remove at the end, as there are 1+h of them 0,1,2,...h unless n//w is smaller than n in which case 
go up to 0,1,2,...n//w e.g. if n = 13 and w = 4 we have counted patterns with all heights =0,1,2 and 3 <- (13//4)

So bads = 1 + min(h, n//w) due to the no-all-same-height condition.
"""
from math import comb
from functools import lru_cache

cache_comb = lru_cache(maxsize=None)(comb) # UPDATE: don't think this caching is needed actually

BIGMOD = 10**9 + 7

def integer_solutions_with_exactly_R_total_ribbon(R, w, h):
    # can stop summation when i == w (binomial coeff) or when R - i*(h+1) < 0 (in the binomial with replacement coeff)
    solutions = 0
    for i in range(min(w + 1, R // (h + 1) + 1)):
        #                                              V V V V V this is comb(n+k-1, k) choose with replacement; here choosing i of the "columns" among w available which will have h+1 cubes in them; thus making them "bad" columns that don't fit in box of max height h, and thus removing them via PIE
        solutions += pow(-1, i) * cache_comb(w, i) * cache_comb(w + R - i * (h + 1) - 1, R - i * (h + 1))
    return solutions % BIGMOD

n, w, h = map(int, input().split())

bad_solutions = 1 + min(h, n // w) # separate PIE calculation: we need to remove the arrangements where all heights are equal

all_integer_solutions_for_up_to_n_total_ribbon = sum(integer_solutions_with_exactly_R_total_ribbon(r, w, h) for r in range(n + 1))

res = all_integer_solutions_for_up_to_n_total_ribbon - bad_solutions

print(res % BIGMOD)