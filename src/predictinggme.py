# Predicting GME
# https://open.kattis.com/problems/predictinggme
# TAGS: dynamic programming
# CP4: 3.5g, DP level 2
# NOTES:
"""
It's the same as:

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

I'm solving with the "state-machine" approach, 3 possible states and then some transititions between them.

Note the 2 allowed self-transitions in addition to the transitions between the states:
you can stay in the same state if you are in states: {skipped,bought}
but you cannot stay in state: {sold}
"""
N = int(input())

xs = map(int, input().split())

skipped, sold, bought =  0, 0, float("-inf")

for x in xs:
    skipped, sold, bought = max(skipped, sold), bought + x, max(bought, skipped - x)

print(max(skipped, sold))