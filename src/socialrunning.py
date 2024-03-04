# Social Running
# https://open.kattis.com/problems/socialrunning
# TAGS: logic, mathematics
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
Rant: I don't think it's a very good pedagogical choice of illustrative example:
The people are indexed 0,1,2,3 but then the DISTANCES are also 1,2,3,4
which makes it look like there is some connection, but there isn't.
Why not use distances 10,17,42,99 to make it clear in the test case.

---

Draw it on paper, for each starting point - say person '0' (label doesn't matter) - the only people who will ever be running alone are:
- the start runner, on their first interval (i.e as they reach the next person)
- the last runner, after they drop off the penultimate runner

-> so basically the only intervals are the '1st' and the 'n-2'nd (NOT THE N-1st!! DRAW IT OUT TO BE CLEAR)

e.g. in the given example if runner3 goes first, then there is:

1 person on interval 3-0, 2 people on 0-1, 3 people on 1-2, 4 people on 2-3, 3 people on 3-0, 2 people on 0-1, 1 person on 1-2. 

In the above list look at the "bookends" -> intervals "3-0" and "1-2" are the only relevant ones
(Again, as explained in Rant above, this n=4 case is confusing. Use n=7 or whatever to make it clearer:
THE 2 OFFSET HERE IS THE FACT THAT WE ARE AT "FIRST" AND "LAST BUT ONE" positions:
so draw e.g. a circle with 7 segments instead of 4 so you don't get confused by where the "2-offset is coming from")

---

Implementation note:

Based on above, just check all possible intervals that are separated by 2 indices
e.g. 0 1 2 3 4 5 6 -> 0&2, 1&3, ...4&6, 5&0, 6&1 (NOTE THE WRAPAROUND)
-> I handle wraparound by zipping over "xs * 2"
"""
n = int(input())

xs = []
for _ in range(n):
    x = input()
    xs.append(int(x))
    
xs = 2 * xs # handle wraparound

res = min(a + b for a, b in zip(xs, xs[2:]))

print(res)