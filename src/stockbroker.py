# Daydreaming Stockbroker
# https://open.kattis.com/problems/stockbroker
# TAGS: logic, greedy
# CP4: 3.4g, Non-Classical, Harder
# NOTES:
"""
It's a variant on "best time to buy stock" classic problem.

Here the reading comprehension is that you have maximum possible amount of stock of the company = 100_000
"""
d = int(input())

prices = []
for _ in range(d):
    x = int(input())
    prices.append(x)

prices.append(-10 ** 9) # create a dummy element, used to trigger pocessing of last real element

qty = 0
cash = 100
prev = 10 ** 9
for x in prices:
    if x > prev:
        # Should have bought as many as possible at `prev` price
        # CARE! max allowed shares is 100_000
        q = (cash // prev)
        q = min(q, 100_000 - qty)
        qty += q
        cash -= q * prev
    else:
        cash += qty * prev
        qty = 0
    prev = x

print(cash)