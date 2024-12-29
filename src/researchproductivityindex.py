# Research Productivity Index
# https://open.kattis.com/problems/researchproductivityindex
# TAGS: dynamic programming, mathematics, probability
# CP4: 8.7k, Three++ Components, E
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/researchproductivityindex.md
"""
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