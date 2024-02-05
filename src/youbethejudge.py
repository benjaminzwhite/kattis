# You Be the Judge!
# https://open.kattis.com/problems/youbethejudge
# TAGS: brute force, string
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
Not sure what to note here - basically it's an input parsing question (the mathematics part is simple).

I'm guessing it's rated at 6ish difficulty due to people solving in C++ rather than e.g. Python.

I got lots of WA: after manually coding as many of the rules as I could interpret from the statement,I found that
having a generic Try/Except handled the leftover testcases (originally I had a Except ValueError specifically, but
this had a few WA, so not 100% sure which testcases cause an exception that is NOT a ValueError O_o)

There's probably a lot of redundant/unneeded stuff in code below therefore.
"""
import sys

def is_prime(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return n > 1

tokens = []
for l in sys.stdin:
    tokens.extend(l.strip().split())

ok = True
if len(tokens) != 3:
    ok = False

if ok:
    for token in tokens:
        if not token.isdigit() or token[0] == '0' or token[0] == '-' or token[0] == '.':
            ok = False

    try:
        res = int(tokens[0])
        if res < 4 or res > 10**9 or res%2 == 1:
            ok = False

        p1, p2 = int(tokens[1]), int(tokens[2])

        if not is_prime(p1) or not is_prime(p2) or p1 + p2 != res:
            ok = False
    except: # ONLY NEEDED TO REMOVE ValueError HERE TO GET ACCEPTED O_o
        ok = False

if ok:
    print(1)
else:
    print(0)
