# Short Sell
# https://open.kattis.com/problems/shortsell
# TAGS: array
# CP4: 3.5a, Max 1D/2D Range Sum
# NOTES:
"""
This is a variation on the theme of "best time to sell stock" type problems.

For ex. on Kattis I've solved Radio Commercials (https://open.kattis.com/problems/commercials) which is very similar, using Kadane's algorithm.

Note that you are *short selling* so you want to sell as high as possible then buy as low as possible.

See comments below also: I don't understand what the "K" variable is doing, AFAICT it's just a linear constant term so nothing interesting
"""
N, K = map(int, input().split())

xs = map(int, input().split())

best_holding = 0
best_profit = 0
for x in xs:
    # 2 options to have as much cash as possible today:
    # 1/ either hold stock from previous day
    # 2/ SELL 100 shares (that you "borrow" short selling) at today's price x
    # UPDATE: NOT VERY CLEAR WHAT THIS K IS: COULDN'T MATCH TESTCASE - IT SEEMS YOU *ALWAYS* PAY K INTEREST ON EVERY DAY???
    # SO IT DOESN'T DO ANYTHING INTERESTING SINCE IT'S JUST A FLAT LINEAR FACTOR ON BOTH OPTIONS ?
    best_holding = max(best_holding, x * 100) - K # <--- in both cases you will pay K interest
    
    # if you BUY STOCK (because we are short selling so BUYING closes the short sell O_o) today:
    # 1/ You have best_holding cash
    # 2/ You spend x*100 to buy 100 units of stock at curr price x
    # 3/ Your profit is therefore best_holding - x*100
    best_profit = max(best_profit, best_holding - x * 100)

print(best_profit)