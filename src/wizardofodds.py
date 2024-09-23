# Wizard of Odds
# https://open.kattis.com/problems/wizardofodds
# TAGS: binary, improve
# CP4: 2.2i, Big Integer
# NOTES:
"""
Binary search reduces number of possible answers by 1/2 at each step which is optimal

TODO: IMPROVE: I want to solve in .cpp

Python specific: this is supposed to be a BigInteger problem as per CP4 list it is harder in real languages.
Basically N <= 10**101 so how you input this from the given string when it doesnt fit in 64 bit is the challenge in other languages.

log2 will be the length of its binary representation (ie up to its MSB), e.g. for n = 10_000 -> "10011100010000" has 14 digits and
we have that ceil(log2(10_000)) = 14 indeed.
"""
from math import ceil, log2

n, k = map(int, input().split())

if k >= ceil(log2(n)):
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")