# Alehouse
# https://open.kattis.com/problems/alehouse
# TAGS: logic, sorting
# CP4: 2.3a, Priority Queue
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/alehouse.md
"""
n, k = map(int, input().split())

xs = []
for _ in range(n):
    l, r = map(int, input().split())
    # NOTE: use op = 1, -1 to determine whether we will increase or decrease the "open/close interval counter"
    xs.append((l, 1)) 
    xs.append((r + k, -1)) # prolong each person's real interval by k to create an effective interval ending at r+k instead

# sortkey below places ARRIVALS (+1) before DEPARTURES (-1) in case of a tie on the arrival time, x. 
# (since you are allowed to "count the person on the way out" you CAN increment first with the new arrival
# so that the total people in shop is BIGGER+1 then SMALLER-1 so that you reach the bigger total first)
xs = sorted(xs, key=lambda x:(x[0], -x[1]))

most = 0
people = 0 # effective people at the current effective time point
for x_eff, op in xs:
    people += op
    if people > most:
        most = max(most, people)

print(most)