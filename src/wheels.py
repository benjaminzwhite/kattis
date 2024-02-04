# Wheels
# https://open.kattis.com/problems/wheels
# TAGS: DFS, mathematics, nice
# CP4: 8.7k, Three++ Components, E
# NOTES:
"""
Nice exercise:

- Start with initial driver wheel - it is CLOCKWISE and has 1 turns per minute
- Maintain wheels[] which is the order in which to display final results
- Maintain res{} which will store for each wheel its TURNS PER MINUTE AND DIRECTION
- Initialize DFS stack with first wheel, then while stack is nonempty: check all other wheels if they are touching the current stack wheel.

DO THIS WITHOUT TAKING SQUARE ROOTS
-> if 2 wheels touch then hypothenuse formed by sum of their 2 radius forms right triangle with dx and dy between the wheel's centres (draw it if you need to)

Each time you find a circle in your current DFS:
- add it to res: you know that its Turns Per Minute will be given by TPM of the touching wheel, times the Fraction(r,r_) of their radius ratios/gearing
- you also know its DIRECTION since it will be opposite to the touching wheel
- MAKE SURE YOU DISCARD THE TOUCHING WHEEL at each step of the DFS so you dont process states more than once

That's it really, just DFS outwards from the start wheel.
At the end, any wheel that is not in res{} cannot be reached/touched from any powered wheel so those wheels will not be moving.

---

Implementation note:

Use 1 for clockwise, 0 for anticlockwise. This is so that I can use XOR on adjacent wheels to change directions 0->1, 1->0.

Use Python Fraction import, for GCD handling.
"""
from fractions import Fraction 

T = int(input())

for _ in range(T):
    n = int(input())

    wheels = []
    res = {} # STORE WHEELS PROCESSED
    to_check = set()

    for _ in range(n):
        x, y, r = map(int, input().split())
        wheels.append((x, y, r))
        to_check.add((x, y, r))

    stk = [(wheels[0], 1)] # first wheel is starter wheel speed 1 -- we say that 1 is CLOCKWISE 0 is ANTICLOCKWISE
    res[wheels[0]] = [1, 1] # 1st elem is turns per minute 2nd elem is 1/0 clockwise anticlockwise

    while stk:
        wheel, direction = stk.pop()
        x, y, r = wheel
        turns_per_minute = res[(x, y, r)][0]
        to_check.discard((x, y, r))

        for (x_, y_, r_) in to_check:
            if abs(x - x_)**2 + abs(y - y_)**2 == (r + r_)**2: # don't need abs() actually O_o
                res[(x_, y_, r_)] = [Fraction(turns_per_minute * r, r_), direction ^ 1] # XOR direction 
                stk.append([(x_, y_, r_), direction ^ 1])

    for w in wheels:
        if w not in res:
            print("not moving")
        else:
            turns_per_minute, direction = res[w]
            if direction == 1:
                c = "clockwise"
            else:
                c = "counterclockwise"
            print(turns_per_minute, c)