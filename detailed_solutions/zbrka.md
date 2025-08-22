# Detailed solution for Kattis - Zbrka

[Problem statement on Kattis](https://open.kattis.com/problems/zbrka)

Nice combinatorics exercise.

## Tags

mathematics, combinatorics

## Solution

For a sequence from 1 to N to have confusion C, consider a sequence of 1 to N-1 and condition on the location of N in that sequence:

- If N is placed at the end, you create 0 new confused pairs since N is bigger than all elements to the left
- If N is placed at -2th position, you create 1 new confused pair since N is always bigger than last element
- If N is placed at -3th position, you create 2 new confused pairs since N is bigger than the last 2 elements etc.

So if T(N,C) counts the number of sequence on {N} with total confusion C then you can reach T(N,C) by adding N to a sequence of since N-1 and, depending on the position, you will need to take a sequence with C-x confusion, i.e.:

```
T(N,C) = T(N-1,C) + T(N-1,C-1) + T(N-1, C-2) + ... T(N-1, C - (N-1) )
         ^^^^^^                     ^^^^
       N in last pos            N in -3th position etc, so need to start with a sequence of C-2 confusion so that adding N leads to C-2+2 = C confusion.
```

For the initial conditions, clearly also: T(1,0) = 1, T(1,1) = 0

Now at this point we're one mathematically but we need to improve/rearrange to avoid having to take many sums and get a faster solution.

So need to try simplifying the recurrence a bit - from here on I'll use T(n,k) to match the definition in the OEIS (see link at the end).

`T(n,k) = sigma(i=0, i=n-1) T(n-1, k-i)`  (our starting point; see above where we derived this - it's just computationally slow_

1. add T(n-1,k-n) to both sides:

`T(n,k) + T(n-1,k-n) = sigma(i=0, i=n) T(n-1, k-i)`

2. substract T(n-1,k) from both sides:

`T(n,k) + T(n-1,k-n) - T(n-1,k) = sigma(i=1, i=n) T(n-1, k-i)`

3. Relabel/shift the righthand side: set i = j+1

`sigma(i=1, i=n) T(n-1, k-i)  ==>  sigma(j=0, i=n-1) T(n-1, k-1-j)  ==>  T(n, k-1)`

So putting this together:

`T(n,k) + T(n-1,k-n) - T(n-1,k) = T(n, k-1)`

or, for dynamic programming implementation, expressing T(n,k) in terms of previously computed elements:

`T(n,k) = T(n, k-1) - T(n-1,k-n) + T(n-1,k)`

Finally, if you look up the first few terms on OEIS, these are indeed known: they are in fact

[https://oeis.org/A008302](https://oeis.org/A008302)

"Triangle of Mahonian numbers T(n,k)"


## AC code

```python
BIGMOD = 10 ** 9 + 7
N_MAX = 1_005
C_MAX = 10_005

# inputs
N, C = map(int, input().split())

# UPDATE: slight optimization - you can't have more than comb(N, 2) pairs so confusion is bounded by this in any case
C = min(C, N * (N + 1) // 2)

# dp is implementing T(n,k) from notes above.
dp = [[0] * C_MAX for _ in range(N_MAX)]
dp[1][0] = 1 # all (there are cnt=1 of them) sequences with N=1 terms i.e. {1} have confusion 0

for n in range(2, N + 1):
    for k in range(C + 1):
        # dp[n][k] = dp[n][k-1] - dp[n-1][k-n] + dp[n-1][k]
        #                                ^^^^^
        # CARE! need to be careful with the k-n term; it wraps around, and only makes sense (see notes above) if k >= n
        # so only do if k>=n:
        dp[n][k] = dp[n][k - 1] + dp[n - 1][k]
        if k >= n:
            dp[n][k] -= dp[n - 1][k - n]

        dp[n][k] %= BIGMOD

print(dp[N][C] % BIGMOD)
```