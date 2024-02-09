# Driver's Dilemma
# https://open.kattis.com/problems/driversdilemma
# TAGS: basic
# CP4: 1.4i, Still Easy
# NOTES:
"""
Reading comprehension:

You have to notice in the first paragraph that "half a tank left" means the car fuel level is always half the maximum capacity.

---

One clean/physical solution approach is to realise that you have an effective "gallon per mile" consumed which depends 
on the actual mpg and the current fuel_leak_per_hour. I left full variable names below for clarity.
"""
capacity, fuel_leak_per_hour, miles = map(float, input().split())

actual_tank = capacity / 2 # haha lol xd
best = None

for _ in range(6):
    mph, mpg = map(float, input().split())

    gpm = 1 / mpg + fuel_leak_per_hour / mph
    
    if actual_tank >= miles * gpm:
        best = int(mph)

if best is not None:
    print("YES", best)
else:
    print("NO")