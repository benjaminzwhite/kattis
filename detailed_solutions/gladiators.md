# Detailed solution for Kattis - Gladiators

[Problem statement on Kattis](https://open.kattis.com/problems/gladiators)

This is a simple combinatorics problem, but it's a nice exercise to work through the recursion logic (and then find that it's on OEIS of course)

## Tags

mathematics, combinatorics

## Solution

As mentioned above, this is a combinatorics reasoning exercise, specifically the Eulerian numbers of the second order:

[https://en.wikipedia.org/wiki/Eulerian_number](https://en.wikipedia.org/wiki/Eulerian_number)

OEIS:

[https://oeis.org/A008517](https://oeis.org/A008517)

**However**, the exercise's indexing is off-by-one (in my opinion) compared to the "logical" recurrence definition:

```
<<m, k>> = (2m-k-1) * <<m-1, k-1>> + (k+1) <<m-1, k>>
           ----- first term -----    - second term - 
```

Let's spell out clearly the combinatorial recursion logic and explain the two terms above.

You build a permutation on multiset `{1,1,2,2,...,m,m}` with exactly `k` ascents by:

- first term: taking a permutation on the multiset `{1,1,2,2...m-1,m-1}` with exactly `k-1` ascents and placing `m,m` in `(2m-k-1)` locations where there is **no** ascent
- second term: or, taking a permutation on the multiset `{1,1,2,2,...m-1,m-1}` with exactly `k` ascents and placing `m,m` in `(k+1)` locations where there is **already** an ascent: the new element `m,m` "kills" one ascent, but creates a new one itself, **for a net change of 0 so you still have `k` ascents**. (e.g. `1122 -> 113322` you lose `11 -> 22` ascent but gain `11 -> 33` for `-1 + 1 == 0` change in ascents)

### Implementation note

The exercise indexing is off by one because it says the "first element itself **always counts as a "rise"** (or whatever the terminology they use)" so it means that e.g. `332211` which in the standard notation is `<<m=3, k=0>>` (only case with m=3 and k=0 ascents), while here **in their interpretation it has** `m=3, k=1` ascent!!

So I just implemented the recursion with the "mathematics convention", and for each of **the exercise's** queries `(m, k)` **my recurrence has the answer as `(m, k-1)` to ignore this "+1" ascent**.

## AC code

```python
M_MAX = 105
K_MAX = 105

dp = [[0] * K_MAX for _ in range(M_MAX)]
dp[0][0] = 1
for m in range(1, 101):
    for k in range(101):
        dp[m][k] = dp[m - 1][k - 1] * (2 * m - k - 1) + dp[m - 1][k] * (k + 1)

T = int(input())
for _ in range(T):
    m, k_ = map(int, input().split())
    # k_ is off by one compared to "usual" k (see NOTES) w.r.t to usual Eulerian definition
    print(dp[m][k_ - 1])
```