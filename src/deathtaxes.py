# Death and Taxes
# https://open.kattis.com/problems/deathtaxes
# TAGS: interpreter
# CP4: 1.4j, Medium
# NOTES:
"""
Just do exactly as it says and reading comprehension:
Small "gotcha" is need to check that profit > 0 at the end, if not you do NOT apply any tax

For numerical precision:
As in code below, it seems you can update the avg_cost as you go along: it passes the accuracy 0.01 at the end so no need to be clever
"""
weighted_price = 0
num_shares = 0
avg_cost = 0

for l in open(0):
    cmd, *xs = l.split()
    if cmd == "buy":
        x, y = map(int, xs)
        avg_cost = ((avg_cost * num_shares) + x * y) / (num_shares + x)
        weighted_price += x * y
        num_shares += x
    elif cmd == "sell":
        x, y = map(int, xs)
        num_shares -= x
    elif cmd == "split":
        x = int(xs[0])
        num_shares *= x
        avg_cost /= x
    elif cmd == "merge":
        x = int(xs[0])
        num_shares //= x
        avg_cost *= x
    else:
        x = int(xs[0])
        profit_per_share = x - avg_cost
        if profit_per_share > 0: # only apply tax if profit > 0
            after_tax = profit_per_share * 0.3
        else:
            after_tax = 0
        res = num_shares * (x - after_tax)
        print(res)
        break