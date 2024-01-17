# The Stock Market
# https://open.kattis.com/problems/borsen
# TAGS: array
# CP4: 0, Not In List Yet
# NOTES:
"""
It's a variant on "Best Time to Buy Stock" type stuff, but a bit hard to follow due to decimals and description.

Reading comprehension of the transaction fee description is important:
IT APPLIES BEFORE YOU BUY but **AFTER** you sell
(I first was trying to ensure you always had cash > transaction fee for selling, but got WA).
"""
N = int(input())
transaction_fee = float(input())

max_cash = 100
max_q = 0

for _ in range(N):
    x = float(input())
    max_cash = max(max_cash, max_q * x - transaction_fee)
    max_q = max(max_q, (max_cash - transaction_fee) / x)

print(max_cash)