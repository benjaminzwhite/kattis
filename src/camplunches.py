# Camp Lunches
# https://open.kattis.com/problems/camplunches
# TAGS: dynamic programming
# CP4: 0, Not In List Yet
# NOTES:
"""
Nice little exercise. A bit of reading comprehension to understand the problem statement though - basically the "real word stuff" AFAICT means:

1. "children get to eat with their friends" => cannot split groups, so either use or do not use group of size S1, S2...

2. "there are no wasted lunches" (?!) => I think it means that if you take a box, with e.g. 17 lunches, then you must use all of them
  IN OTHER WORDS: the total number of people you take must be divisible by the number of lunches, so that you take an INTEGER NUMBER OF BOXES
  e.g. if 17 lunches per bin, you can take 17, 34, 51... people out so that there will be no wastage

3. there is another constraint of "min/max number of people allowed" also:
  CARE!: the "max number" might be effectively lower than the given one, since the max is also constrained by max number of lunches:
  -> update a variable UPPER_RANGE for the binary search by looking at which of the 2 variables is SMALLER: min(max_people, num_bins * num_lunches_per_bin)
  -> also: MAKE SURE YOU ITERATE OVER MULTIPLES OF num_lunches_per_bin (in particular, start your upper_range so that it is the 
     smallest number <= upper_range that is divisible by lunches_per_bin)

---

Implementation note:

For the recursive solve() remember to add a check for "curr_sum > target" to allow you to RETURN FALSE EARLY
Otherwise solution will run realy slow as it checks entire xs for values that clearly can't be valid.

e.g. if target = 38 and your curr_sum is already 319183 then you can stop early !
"""
from functools import lru_cache

# dynamic programming solver
def solve(target, xs):
    @lru_cache # UPDATE: don't think this is needed actually
    def helper(idx, curr_sum):
        if curr_sum == target:
            return True
        elif curr_sum > target or idx >= len(xs):
            return False

        return helper(idx + 1, curr_sum + xs[idx]) or helper(idx + 1, curr_sum)

    return helper(0, 0)

# inputs
n = int(input())
xs = list(map(int, input().split()))
num_bins, lunchs_per_bin, min_people, max_people = map(int, input().split())

# you don't need to binary search it seems because the range is small
flg = False
UPPER_RANGE = min(num_bins * lunchs_per_bin, max_people)

# all values need to be divisible by lunches per bin
if UPPER_RANGE % lunchs_per_bin != 0:
    UPPER_RANGE -= (UPPER_RANGE % lunchs_per_bin)

# the question asks for the LARGEST number of students, compatible with the requirements
# so iterate DOWNWARDS in range, in increments of -lunchs_per_bin (since needs to be multiple of this number, see NOTES above)
for guess in range(UPPER_RANGE, min_people - 1, -lunchs_per_bin):
    if solve(guess, xs):
        flg = True
        res = guess
        break

if flg:
    print(res)
else:
    print("impossible")