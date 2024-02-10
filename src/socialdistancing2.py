# Social Distancing
# https://open.kattis.com/problems/socialdistancing2
# TAGS: array
# CP4: 1.4f, Function
# NOTES:
"""
Hard part is to handle the count of seats between the "last -> first" of the given xs
e.g. if there are 9 "real" seats and {2, 6} are occupied then there are 3 real seats free between 2 -> 6
But how many between 6 -> 2 (passing through 7,8,9,1) ? Answer is 4 in this case.

I implement this by appending to xs (the occupied "real" seats) a "dummy" occupied seat, which is at the same "location/distance" as xs[0] is.

i.e. in this case I am appending a dummy seat = "11" such that 6 -> 11 has 4 free seats between them; which mimics move from 6 -> 2 passing through 9.

Then the formula for each interval is simple - it's (second - first - 2) // 2.
Explanation for why I use -2 instead of -1:
e.g. 2 -> 6 is 3,4,5 i.e. there are 6-2 - 1 = 3 actual seats but if you do -2 instead of -1 you handle the cases
where there are 2 actual seats (which allows 0 new people to sit down) - this is just a nice trick to avoid doing various adjustments etc.
"""
seats, _ = map(int, input().split())
xs = list(map(int, input().split()))

effective_xs = xs + [seats + xs[0]] # append a dummy occupied seat of the correct value, see notes above.

res = 0
for fst, snd in zip(effective_xs, effective_xs[1:]):
    res += (snd - fst - 2) // 2

print(res)