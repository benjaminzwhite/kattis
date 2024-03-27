# Cardboard Container
# https://open.kattis.com/problems/cardboardcontainer
# TAGS: brute force, mathematics, number theory, improve
# CP4: 9.sqrt, Square Root Decomp
# NOTES:
"""
TODO: IMPROVE:

Brute force - after solving, I also found the OEIS page https://oeis.org/A075777
-> doesn't seem to be a smarter way of finding it O_o
"""
v = int(input())

best = float('inf')

for x in range(1, int(v**0.5) + 1):
    for y in range(1, int(v**0.5) + 1):
        z, r = divmod(v, x * y)
        if r == 0:
            surface = 2 * (x * y + y * z + z * x)
            best = min(best, surface)

print(best)