# Time Travelling Temperatures
# https://open.kattis.com/problems/temperature
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
"""
Reading comprehension:

Basically it seems that T_A is a linear temperature scale t, and T_B is of the form Y*t + X
So the temperature at which both are the same means (if we take T_A to be the reference linear one) ,  where it T_B = Y*t + X == t
-> solving gives t = -X/(Y-1)
-> this is impossible if Y==1 (lines are parallel) unless X==0 also in which case the lines are collinear
-> otherwise solution (intersection point) is unique
"""
X, Y = map(int, input().split())

if Y == 1:
    print("ALL GOOD" if X == 0 else "IMPOSSIBLE")
else:
    print(-X / (Y - 1))