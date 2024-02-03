# Planting Trees
# https://open.kattis.com/problems/plantingtrees
# TAGS: basic, logic
# CP4: 1.4e, Control Flow
# NOTES:
"""
Not sure if this is a troll question/logic test/or maybe the authors missed the simple solution O_o:

Since the records stop when there is a winner, then the last person to play must have won the game
"""
inps = input()
# A2B1A2B2A1A2A2A2
#               ^
#               |__ inps[-2] : this is always the name (A/B) of the last person to play, so it is the winner.
res = inps[-2]

print(res)