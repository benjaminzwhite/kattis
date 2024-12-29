# Detailed solution for Kattis - Research Productivity Index

[Problem statement on Kattis](https://open.kattis.com/problems/researchproductivityindex)

Nice dynamic programming exercise, it is very similar to `Kattis : Genius`, which I have already solved - some of the comments in `genius.py` therefore can be reused here.

## Tags

dynamic programming, mathematics, probability

## Solution

As mentioned above, this exercise is very similar to `Kattis : Genius` exercise. In that previously solved exercise, as we increase "rows" i.e. process more tournaments, we obtain non-zero probability in states corresponding to 1, then 2, then 3 correct predictions i.e. columns 1,2,3..

The result is additive probability in the final, t'th, row - all the states which have `k_ >= k` (where `k` is from statement; i.e. the min number of correct predictions needed to win the Genius game etc.).

Using the same logic for this exercise:

- `dp[subm][acc]` is the probability to have exactly `acc` accepted papers accepted having submitted `subm` papers
- **Initial condition is:** `dp[0][0] = 1`, all the probability is in this initial state
- The transition is: `dp[subm][acc] = dp[subm-1][acc] * (1 - prob_curr_is_accepted) + dp[subm-1][acc-1] * (prob_curr_is_accepted)`

To explain the transition rule above, the 2 components are, respectively:

1. go from state with `acc` accepted to **same number, `acc`, accepted**, but with 1 more submission: corresponds to case where this `curr` is **not accepted**
2. go from state with `acc-1` accepted to `acc` accepted, this is case where current paper **is accepted**


## AC code

```python
num_papers = int(input())

papers = list(map(int, input().split()))
papers = sorted(papers, reverse=True) # we will try submitting the papers in order of HIGHEST PROBABILITY FIRST

dp = [[0] * (num_papers + 5) for _ in range(num_papers + 5)] # +5 is sentinel
dp[0][0] = 1 # initial condition, see notes above

for num_submitted, prob_acc in enumerate(papers, 1):
    for acc in range(num_papers + 1):
        dp[num_submitted][acc] += dp[num_submitted - 1][acc] * (1 - prob_acc / 100)
        if acc > 0: # CARE! index acc-1, there is no state where num_accepted is < 0 !!!!
            dp[num_submitted][acc] += dp[num_submitted - 1][acc - 1] * (prob_acc / 100)

res = 0
for num_submitted, acc_data in enumerate(dp[1:], 1):
    expected_prod_index = sum(p * a**(a / num_submitted) for a, p in enumerate(acc_data[1:], 1))
    res = max(res, expected_prod_index)

print(res)
```
