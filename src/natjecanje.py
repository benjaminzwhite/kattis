# Natjecanje
# https://open.kattis.com/problems/natjecanje
# TAGS: logic, greedy
# CP4: 3.2k, Backtracking (Easier)
# NOTES:
"""
Nice little puzzle. Thought about it, noticed that "greedy" always works:

For each damaged kayak, you must check first if there is repair with same number - if so remove both damaged and reserve (with same number).

NOW: notice that IT IS ALWAYS WORTH TAKING THE d-1 KAYAK IF IT IS AVAILABLE, before trying the d+1, because if you take d+1 FIRST, then
you can miss out on some pairings, but this is not the case if you take the d-1 kayak first. 

All cases are illustrated with the given example with two damaged kayaks {2,4} and 3 repair kayaks {1,3,5}:

              2 4
             1 3 5

Imagine all combinations where {1,3,5} do or do not appear:
- 1, 3, 5 alone -> damaged pairing with leftmost available always removes 1 pair in any case
- {1,5} or {3,5} -> again doing Greedy always removes 2 pairs in all cases
- {1,3} -> this is the interesting case: if you take "d+1" 2 -> 3 instead of "Greedy d-1" 2 -> 1 then you deny the ability of 4 to pair with 3.
  I.e. {2->1, 4->3} removes 2 pairs, but {2->3} means {4->X} fails (since 5 is not available in this situation)

Finally, for an arbitrary arrangement this is the case (since arbitrary arrangement always has this zigzag pattern once
you remove the identical TOP = BOTTOM elements.)
"""
N, S, R = map(int, input().split())

damaged = list(map(int, input().split()))
d_set = set(damaged)

reserve = set(map(int, input().split()))

for d in damaged:
    if d in reserve:
        d_set.discard(d)
        reserve.discard(d)
    elif d - 1 in reserve:
        d_set.discard(d)
        reserve.discard(d - 1)
    elif d + 1 in reserve:
        d_set.discard(d)
        reserve.discard(d + 1)

print(len(d_set))