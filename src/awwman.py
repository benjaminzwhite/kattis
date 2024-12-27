# Aww Man
# https://open.kattis.com/problems/awwman
# TAGS: logic
# CP4: 0, Not In List Yet
# NOTES:
"""
Seems a bit overranked - maybe hard to notice simple solution in the competition environment (CodeSprint LA 2021):

Just have to reading comprehension that N is total hours in "total day" (ie dayTIME+nightTIME), that dayTIME is N-M and nightTIME is M,
and also that you can have b < a since "b is time of day" and YOU MAY ARRIVE SEVERAL DAYS LATER SO it's the MOD N behavior that you need.
"""
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a, b, d = map(int, input().split())

    travel_delta = (b - a)

    if travel_delta < 0:
        travel_delta += N

    arrival_time = (b + d + travel_delta) % N

    if arrival_time < 0:
        arrival_time += N

    if arrival_time <= (N - M):
        print("YES")
    else:
        print("NO")