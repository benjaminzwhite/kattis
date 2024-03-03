# Less vs. Fewer
# https://open.kattis.com/problems/lessvsfewer
# TAGS: basic, dict
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
"""
Instead of adding "number of" and "amount of" to d -> I just add first word
This makes it easier to use split() on the input lines later on (see comment below)
"""
REF = {"number":"c","amount":"m","most":"cm","fewest":"c","least":"m","more":"cm","fewer":"c","less":"m","many":"c","much":"m","few":"c","little":"m"}

n, q = map(int, input().split())

d = {}
for _ in range(n):
    noun, x = input().split()
    d[noun] = x

for _ in range(q):
    *ref, noun = input().split()
    # !!! note that ref may have more than 1 item in it due to NUMBER OF and AMOUNT OF so only lookup first element ref[0] in REF
    if d[noun] in REF[ref[0]]:
        print("Correct!")
    else:
        print("Not on my watch!")