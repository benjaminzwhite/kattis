# Detailed solution for Kattis - Permutation Descent Counts

[Problem statement on Kattis](https://open.kattis.com/problems/wordspin)

Just a nice combinatorics exercise, good practice finding the recursion relation.

## Tags

mathematics, combinatorics

## Solution

To get a permutation of `{1,2,..N}` with `v` descents you can either:

**A)** start with a permutation of `{1,2,..N-1}` with `v` descents and add the `Nth` element such that it does **not** create a new descent.

Focus on the `N-1 + 1 = N` positions to place next element (usual "stars and bars" combinatorics approach):

e.g. suppose we have a case with `N = 6` so also `N-1 = 5`

`53412` : let's make the descents clearer with `|` : `_5|3_4|1_2_`  here there there 2 descents: `5 -> 3` and `4 -> 1`.

If you place `6` in any of the `v` locations `|` that separate a current descent e.g. `5|3 : 563`  or `4|1 : 461`, **or in the 1 location `_` at the END of the permutation** you do **not create a new descent** since you just replace the "large left element" with an even larger one. In this case A) there are `v+1` such locations.

**B)** start with a permutation of `{1,2,..N-1}` with `v-1` descents, and add the `Nth` element such that it **does** create +1 new descents.

So takeing the above reasoning in "opposite" direction, you can do this by placing `N` in any of the positions `_` which **do not separate a current descent**.

Since there are `N-1 + 1 = N` total positions, and `v-1` descents which means `v-1 + 1 = v` of the positions (including at the end), which **do** separate
a current descent, there are therefore `N - v` available positions which **do not separate** a current descent. This is where we can place the `Nth` element to create +1 new descent.

Hence the recursion is `p(N, v) = "case A" + "case B" = p(N-1, v) * (v+1) + p(N-1, v-1) * (N-v)`


## AC code

```python
BIGMOD = 1001113
N_MAX = 105

dp = [[0] * N_MAX for _ in range(N_MAX)]
dp[1][0] = 1

for N in range(2, N_MAX):
    for v in range(N):
        dp[N][v] = dp[N - 1][v] * (v + 1) + dp[N - 1][v - 1] * (N - v) # note should do % BIGMOD here but Python "big int" works without it

T = int(input())
for _ in range(T):
    t, N, v = map(int, input().split())
    print(t, dp[N][v] % BIGMOD) # see comment above, should take modulus earlier
```