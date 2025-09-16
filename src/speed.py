# Need for Speed
# https://open.kattis.com/problems/speed
# TAGS: binary search, improve
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
TODO: IMPROVE: my binary search implementation isn't very good I think; need to improve how I handle
these kind of exercises where there are floats (to avoid numerical issues etc.).

Also based on problem statement I don't think there should be a ZeroDivisionError exception, so maybe
can rewrite to avoid division by small values.

---

It's mainly reading comprehension to understand what is being asked and handle various cases.
"""
n, t = map(int, input().split())

# CARE! reading comprehension to find what value to initialize the "lo" with
# See comments below to explain how the "lo" value gets changed from the input() steps
lo, hi = 1e9, 1e9

xs = []
for _ in range(n):
    dist, speed = map(int, input().split())
    # READING COMPREHENSION: 
    # Note that while Sheila’s speedometer might have negative readings, her true speed was greater than zero for each segment of the journey.
    # -> I take this to mean that in the inputs, if you have a speedometer speed of -145 then the constant c must be at least +145
    # otherwise s+c would be < 0 which is UNPHYSICAL.
    # Similarly if you have a speedometer speed of +23 then the constant c must be at least -23 since otherwise s+c would be < 0 also
    # => SO YOU TAKE THE NEGATIVE OF THE SMALLEST "speedometer" SPEEDS TO HANDLE BOTH CASES.
    lo = min(lo, speed)
    xs.append((dist, speed))

# See above comment for why we negate the current value of "lo" for the binary search:
# if smallest speedometer speed is -145 then c is at least +145
# if smallest speedometer speed is +23  then c is at least -23
lo = -lo

# ---
# Binary search implementation comment:
# the epsilon approach didn't work for me, gets TLE:
# have to do "number of RUNS" binary search (Halim CP4 book talks about this, to avoid precisely this TLE possibility/numerical issues)
#EPS = 1e-10
#while (hi - lo) > EPS:
# ---
RUNS = 200
for _ in range(RUNS):
    c = (hi + lo) / 2

    curr_t = 0
    for dist, speed in xs:
        try:
            curr_t += dist / (speed + c)
        except ZeroDivisionError: # first testcase gave an error on one trial while debugging the hi/lo range configuration, so just in case.
            curr_t += dist / (speed + c + 1e-7)

    if curr_t > t:
        lo = c
    else:
        hi = c

print(c)