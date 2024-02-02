# Welcome to Code Jam (Easy)
# https://open.kattis.com/problems/welcomeeasy
# TAGS: dynamic programming, string
# CP4: 8.3a, DP level 3
# NOTES:
from functools import lru_cache

def solve(ref, s):
    @lru_cache
    def helper(i_ref, i_s):
        if i_ref >= len(ref):
            return 1
        elif i_s >= len(s):
            return 0

        can_use = 0
        if ref[i_ref] == s[i_s]:
            can_use = helper(i_ref + 1, i_s + 1)

        return helper(i_ref, i_s + 1) + can_use
    return helper(0, 0)

ref = "welcome to code jam"

T = int(input())

for t in range(1, T + 1):
    s = input()
    res = solve(ref, s) % 10_000 # last 4 digits wanted
    print(f"Case #{t}: {str(res).zfill(4)}")