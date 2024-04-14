# Fishmongers
# https://open.kattis.com/problems/fishmongers
# TAGS: sorting, greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
Greedy matching - sell as many fish as possible to highest buyer as long as he is willing to buy
"""
n, m = map(int, input().split())

weights = map(int, input().split())
weights = sorted(weights, reverse=True)

fishmongers = []
for _ in range(m):
    qty, price = map(int, input().split())
    fishmongers.append((price, qty))

fishmongers = sorted(fishmongers, reverse=True)

money = 0
i_fishmonger = 0
i_items = 0
while i_fishmonger < len(fishmongers):
    price, buy_qty = fishmongers[i_fishmonger]
    while i_items < n and buy_qty > 0:
        money += weights[i_items] * price
        i_items += 1
        buy_qty -= 1
    i_fishmonger += 1

print(money)