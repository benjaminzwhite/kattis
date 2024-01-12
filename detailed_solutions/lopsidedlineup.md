# Detailed solution for Kattis - Lopsided Lineup

[Problem statement on Kattis](https://open.kattis.com/problems/lopsidedlineup)

This is an excellent "algorithmic" exercise, because it illustrates a very important and useful general technique in problem solving: you should always try, when approaching a difficult question, to think about how to re-arrange/re-define the inputs that you are given.

You can ask things like "how could I make this easier to solve?" or "what would it look like if I already had a correct solution?".

For questions involving specifically involving rows and columns, or matrices in general, you can always create a few of your own testcases with easy-to-work-with layouts (e.g. all 1's and 0's, or triangular matrix, or whatever) and see if you can get some insight into the solution by working with it.

So for this exercise: the "a-ha" insight is to say "What does the table look like when I know the `n/2` Winner and Loser teams ?". As explained below, you can **RELABEL AND REORGANIZE THE ROWS AS YOU WANT** which quickly leads to a good solution approach.

## Tags

logic, proof

## Solution

As explained in the introduction, **assume you have found the optimal solution** and place the players from the "Winner team" (without loss of generality) in top `n/2` rows and place the players from the "Loser team" in the bottom `n/2` rows.

**You now have created 4 distinct regions, which are very easy to work with:**

```
N=6       W11 W12 W13 | W1_L1 W1_L2 W1_L3
          W21 W22 W23 |   etc. ^^^____ cross-terms where a Winner is paired with a Loser so terms DO NOT contribute to this Winner team's strength
          W31 W32 W33 |
          ____________|________________

    L1_W1 L1_W2 L1_W3 | L11 L12 L13   <-- Loser 1 with Loser 2,3 contributions to this Loser team's strength
                      | L21 L22 L23
          etc.        | L31 L32 L33

          ^^^____  cross-terms where a Loser is paired with a Winner, so terms DO NOT contribute to this Loser team's strength  
```

Now, recall that the problem asks to find the "maximum possible difference in strength between two teams of equal size", which in our layout notation above is: `sum(WW_ij) - sum(LL_ij)` (and is the difference of the sums of the top-left and the bottom-right regions in our layout).

With the above decomposition into 4 regions you see that **for any assignment of the rows** the other 2 regions which involve cross terms `Wi_Lj` and `Li_Wj` will **contribute the exact same total score** to the total `n/2` row sum.

(Just to be clear: this is because what we are labelling as `Wi_Lj` or `Li_Wj` above is what the problem calls `c_ij` - we're just using W and L labels to track where this value is in the board - and so since problem says that `c_ij == c_ji`, for us we have that the term e.g. `W1_L2 == L2_W1`)

We can pad these 2 values we want e.g. `sum(WW_ij)` and `sum(LL_ij)` with 2 dummy variables involving cross-terms: `sum(Wi_Lj)` and `sum(Li_Wj)`, to create: `sum(WW_ij) + sum(Wi_Lj)` and `sum(Li_Wj) + sum(LL_ij)`.

Since, as stated above, these 2 dummy variables are equal (so `sum(Wi_Lj) - sum(Li_Wj) == 0`) we have therefore that **maximizing `sum(WW_ij) - sum(LL_ij)` is the same as maximizing `(sum(WW_ij) + sum(Wi_Lj)) - (sum(Li_Wj) + sum(LL_ij))`**

And finally, **we note that these 2 expressions are just the row sums of the first `n/2` rows amd the last `n/2` rows respectively!**

So to maximize the differences of the row sums you just need to put the **largest row sums in the first `n/2` rows and the smallest row sums in the last `n/2` rows.**


### Implementation note

CARE! with the above logic, e.g. each `WW_ij` term appears symmetrically as `WW_ji` also, so we end up **double counting all contributions to the team scores** so we will need to divide our final result by `2`.

## AC code

```python
n = int(input())

row_sums = []
for _ in range(n):
    row_sums.append(sum(map(int, input().split())))

row_sums = sorted(row_sums)

losers = sum(row_sums[:n//2])
winners = sum(row_sums[n//2:])

print((winners - losers) // 2) # CARE! See Implementation note above.
```