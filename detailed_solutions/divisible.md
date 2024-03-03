# Detailed solution for Kattis - Divisible Subsequences

[Problem statement on Kattis](https://open.kattis.com/problems/divisible)

A good exercise involving prefix sums and divisibility properties.

## Tags

mathematics, array, prefix sum

## Solution

The key observation you need to make is: **an interval from `i` to `j` is divisible by `d` if `sum(to j) - sum(to i)` is divisible by `d`.**

(So already you can guess that it makes sense to compute the prefix sums of the input array (i.e. accumulate the values))

If we let `J` be the sum up to the `j`th index and `I` be the sum up to `i`th index, then: if `J = k * d + r` and `I = l * d + s` then `J - I = (k-l) * d + (r-s)`. So by our initial observation, we need `r == s mod d` for this interval `i:j` to be divisible by `d`.

Conversely, given any 2 prefix sums in the array, `I` and `J`, if they belong to the same residue class mod `d`, then you can pick them as the 2 endpoints of a subsequence with the desired divisibility property (since the sum of all the elements between `I` and `J` don't change the residue class, then that sum must have `residue == 0` i.e. be divisible by `d`, as required).

So we conclude that there are as many subsequences as there are ways of choosing a pair of 2 distinct endpoints within each residue class i.e. `sum( comb( num_endpoints_mod_m, 2) for m in range(0, d) )`.

In other words, just accumulate the `xs` and take the `accumulate(xs) % d` element-wise and count how many of each residue `0, 1, ... d-1` there are.

### Implementation notes

You can do this `% d` check "locally" at each `x`, to avoid huge totals in `accumulate(xs)` (since input `x` values can be `10**9` each).

Also, slight subtle point while debugging: you need to increment the `mod_d` count for `residue == 0` by +1 at the start.
This corresponds to the "invisible" endpoint outside the leftmost part of the array with `residue == 0` i.e. when you sum all the elements up to some right index `j`.

e.g. `[1,2,3]` with `d = 6` is 1, because you can have `<start> 1,2,3 <end>`: the modulo of the accumulate when you are at `x=3` is `1+2+3 % 6 = 0` and it can be paired with this leftmost "dummy 0" which is "on the left, outside of the actual array".

## AC code

```python
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
```