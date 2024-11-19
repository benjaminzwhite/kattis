# Careful Ascent
# https://open.kattis.com/problems/carefulascent
# TAGS: simulation, mathematics
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
You can solve with binary search but if you think about it you can solve analytically also:

Since all the terms are linear, calculate where you end up (x coord) for a horiz_velocity of 1, then just
rescale the velocity by (desired_x / reached_x_at_horiz_velocity_1 )

You don't need to sort the "slow-down zones" - just track how much total of the vertical y range they use up - then anything leftover
must be NON-zone i.e. "normal" range - we know in such ranges the horizontal speed is always multiplied by f=1

So implement this by decrementing original y by (u-l) for each slowdown zones upper and lower limit
at end: new y = original y - sum(all y covered in slowdown zones)

To recap - this approach guesses for horizontal velocity = 1 unit/time, then sees what x value, x_at_v_one, we land at, then RESCALES
the HORIZONTAL VELOCITY = 1 by a linear factor (x/x_at_v_one) <--- x here is the desired target x.

Think of it geometrically - draw the line path, then perform a horizontal strech or compression by the found linear factor to
make the path touch the desired x point
"""
x, y = map(int,input().split())

n = int(input())

x_at_v_one = 0

for _ in range(n):
    l, u, f = map(float, input().split())
    y -= (u - l)
    x_at_v_one += (u - l) * f

x_at_v_one += y * 1 # remaining value of y is travelled at "speed" f=1

print(x / x_at_v_one)