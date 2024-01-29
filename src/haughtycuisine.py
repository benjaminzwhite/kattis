# Haughty Cuisine
# https://open.kattis.com/problems/haughtycuisine
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
"""
Weird exercise O_o 

You can just print first line of input - doesn't test for randomness or anything

(For Python at least) you don't need to exit/handle the rest of the I/O
"""
n = int(input()) # not used but left for clarity

s = input() # first line of input is a valid menu, so just multiline print it

print(*s.split(), sep='\n')