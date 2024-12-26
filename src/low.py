# Low Power
# https://open.kattis.com/problems/low
# TAGS: binary search, greedy, nice
# CP4: 8.7b, BSTA+Other, Harder
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/low.md
"""
machines, batteries_per_chip = map(int, input().split()) # n, k in text: was getting confused by variable names so changed

xs = sorted(map(int, input().split()))

num_batteries = len(xs)

lo = 0
hi = 9 * 10**9

while lo < hi:
    curr_d = (lo + hi) // 2 # see NOTES for what we are binary searching on

    i = 0
    ok = True
    
    spare_capacity = 0 # see NOTES: this is the current cnt of total _ in which to place un-pairable batteries (this + and - as you go through xs)
    while i < num_batteries - 1: # Note: need -1 because are comparing i+1 with i
        if xs[i + 1] - xs[i] <= curr_d:
            # this pair can serve as the 2 minimal chips of a new machine, if needed
            spare_capacity += 2 * batteries_per_chip - 2 # each machine has 2 chips with batteries_per_chip batteries: we place the 2 minima, and have 2*b-2 leftover _ spaces
            i += 2 # we move on to next unused battery
        else:
            i += 1 # we cannot use the LEFT battery (see example with 10,30 and 30,41 <-- note in 30,41 we end up using 41 with 42, it is the LEFT/smaller one that is ruled out)
            spare_capacity -= 1 # we must place this unpairable battery somewhere in an existing _
            if spare_capacity < 0:
                ok = False
                break

    if ok
        # curr_d works and can try a SMALLER curr_d inclusive:
        hi = curr_d
    else:
        # curr_d does NOT work so move range
        lo = curr_d + 1

print(lo)