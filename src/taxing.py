# Taxing Problem
# https://open.kattis.com/problems/taxing
# TAGS: binary search
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
It's not difficult but I'm guessing other people had the same experience as me hence why the rating is so high:
it is an annoying exercise, for 2 reasons:

---

Firstly it's unclear, even for a native speaker, trying to understand the IRL stuff and different wording:

- we are told about: "amount he wants each friend to walk away with" as stated what you want to work with
- then we are told: "the amount of money they should receive after tax respectively" in the Input section
- then "the amount of money George will give to his friend, in order to arrive at the correct amount after they have paid tax" in Output

IT'S SO UNCLEAR. Here is what the question is actually asking:

"Person currently earns X BEFORE tax, and f(X) AFTER tax. [where f(X) is some complicated function]
By what AMOUNT does their BEFORE tax income have to increase by, so that their AFTER tax income increases by a SPECIFIED_AMOUNT"

The answer then is:

Just simulate different increases to their BEFORE tax income using binary search, and see what their AFTER tax income is during the binary search.

---

The second reason it's annoying is that I got a bunch of WA just by trying to find the correct starting value for the "hi" of the binary search:

I tried 9e15: that times out.
9e9: gives WA, etc...

Maybe I'm missing something but AFAICT the range is set by the case where you would
e.g. have tiny band and all income taxed at 99.999% (as stated in problem statement) and they are looking to earn 10**6

but I don't see how you get values > 9e9 from this requirement???
"""
t = int(input())

taxbands = []
for _ in range(t):
    size, pc = map(float, input().split())
    taxbands.append((size, pc * 0.01 )) # UPDATE DURING DEBUG: THE VARIABLES ARE FLOATS AND ARE *NOT* YET DIVIDED BY 100 -.-

P = float(input()) * 0.01

F = int(input())
for _ in range(F):
    earned, SPECIFIED_AMOUNT = map(float, input().split()) # see NOTES for variable names; here "earned" is BEFORE tax 

    EPS = 1e-8

    earned_ = earned
    after_tax_no_gift = 0
    for size, pc in taxbands:
        taxable = min(size, earned_)
        earned_ -= taxable
        after_tax_no_gift += taxable * (1 - pc)
        if earned_ <= 0 + EPS:
            break
    if earned_ > 0:
        after_tax_no_gift += earned_ * (1 - P)

    lo, hi = 0, 9e13 # FOUND EMPIRICALLY THAT 9e13 WORKS BUT e.g. 9e9 DOES NOT (also, higher values time out)
    for _ in range(200):
    #while (hi - lo) > EPS:
        mid = (lo + hi) / 2

        total = earned + mid # this is amount you "simulate" that the person earns before tax, if they have an additional '+mid' amount.
        after_tax_w_gift = 0
        for size, pc in taxbands:
            taxable = min(size, total)
            total -= taxable
            after_tax_w_gift += taxable * (1 - pc)
            if total <= 0 + EPS:
                break
        if total > 0:
            after_tax_w_gift += total * (1 - P)

        net = after_tax_w_gift - after_tax_no_gift 

        if net > SPECIFIED_AMOUNT:
            hi = mid
        else:
            lo = mid

    print(lo)