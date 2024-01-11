# Soda Slurper
# https://open.kattis.com/problems/sodaslurper
# TAGS: logic
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
I think it allows an algorithmic/simulation loop approach, but this is an O(1) solution:

If you need C old bottles to make 1 new bottle, then C old bottles also give 1 OLD bottle, after using the new one.

So it actually "costs" C-1 old bottles to make a new bottle, so long as you have at least 1 "infinite" old bottle.

(This is a classic exercise, often done with cigarettes rather than bottles O_o)
"""
init_empty = input()
find_empty = input()
conversion_rate = input()

res = (init_empty + find_empty - 1) // (conversion_rate - 1)

# CARE! edge case - you need to handle the case init_ and find_ are both 0:
# the formula above gives -1, but correct answer is 0
print(max(0, res))