# Divisible Subsequences
# https://open.kattis.com/problems/divisible
# TAGS: mathematics, array, prefix sum, nice
# CP4: 5.3k, Divisibility Test
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/divisible.md
"""
c = int(input())

for _ in range(c):
    d, n = map(int, input().split())
    xs = map(int, input().split())

    residues_mod_d_cnt = [0] * d
    residues_mod_d_cnt[0] += 1 # corresponds to not taking any element from the front; i.e. you can pair off any later index which has %d == 0 with the entire leftmost part of the array

    acc = 0
    for x in xs:
        acc = (acc + x) % d
        residues_mod_d_cnt[acc] += 1

    res = 0
    for m in residues_mod_d_cnt:
        res += m * (m - 1) // 2
    print(res)