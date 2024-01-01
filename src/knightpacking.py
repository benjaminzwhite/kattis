# Knight Packing
# https://open.kattis.com/problems/knightpacking
# TAGS: basic, game, proof
# CP4: 5.7a, Game Theory (Basic)
# NOTES:
"""
For any location, if player 1 can place a knight then player 2 can place a knight in the diametrically opposite location.
For an even number of squares, player 1 runs out of squares first. Vice versa for odd number of squares, player 2 loses.
"""
n = int(input())

res = "first" if n % 2 == 1 else "second"

print(res)