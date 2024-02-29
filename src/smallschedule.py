# Small Schedule
# https://open.kattis.com/problems/smallschedule
# TAGS: mathematics, logic, proof
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
Here is a "proof without words" that you can use to find the analytical solution.

I left meaningful variable names so the logic should be clear.

 <--q--><--q--><--q-->
^
| _____  _____  _____ 
| _____  _____  _____ 
m _____  _____  _____ 
| _____  _____  .....  <-- illustration where the s 1 minute tasks represented as . can fit within the "gaps" left by the large tasks
| _____  _____  ...        (If they dont fit, imagine overflowing and creating new columns of width <--1--> instead of <--q-->)
v

"""
from math import ceil

# CONFUSING VARIABLE NAMES FROM INPUT:
# q is TIME FOR "BIG TASKS"
# m is HOW MANY MACHINES
# s is HOW MANY SMALL (1 second) TASKS
# l is HOW MANY BIG (q second) TASKS
q, m, s, l = map(int, input().split())

# need this many time to fit all the long ones:
time_slots = ceil(l / m)

# in real time this takes up:
long_time = q * time_slots

# can you fit in the s * 1 remaining small tasks in the gaps?
unused_machines = -l % m
avail_small_time = unused_machines * q

if s <= avail_small_time:
    res = long_time
else:
    res = long_time + ceil((s - avail_small_time) / m) # the leftover small time tasks increment by 1 second and can fit m of them into a "column"

print(res)