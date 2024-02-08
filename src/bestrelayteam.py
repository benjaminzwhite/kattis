# Best Relay Team
# https://open.kattis.com/problems/bestrelayteam
# TAGS: sorting, brute force
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
Basically brute force but if you sort the best_second_leg times in ascending order then you can sum the best_three once, then you can compare
the 5th, 6th, .... runners FIRST TIME + sum(best_three) without needing to do lots of loops.

---

Implementation note:

Handle the first i<4 indices separately since there may be a runner with best first and second times (see code, it makes 
sense when you read rather than describe)

(essentially with i < 4 we need to add, NOT the 3 best_THREE_second_leg, but the 3 runners from top 4 i.e. "BEST_THREE_EXCLUDING THE CURRENT i RUNNER")
"""
N = int(input())

xs = []
for _ in range(N):
    name, f, s = input().split()
    xs.append((name, float(f), float(s)))

xs = sorted(xs, key=lambda t:t[2]) # t[2] is the s time i.e. the time on the second_leg -> sort in ascending order of this time
best = float("inf")
runners = []
best_three_second_leg = sum(t[2] for t in xs[:3]) # for all runners outside of best_three second leg, we compare the result of THEIR FIRST LEG TIME + sum(best_three_second_leg)

for i, x in enumerate(xs):
    _, f, s = x
    if i < 4:
        curr = f + sum(t[2] for j, t in enumerate(xs[:4]) if j != i) # with i<4 we need to add not the best_THREE_second leg but the "BEST_THREE_EXCLUDING THE CURRENT i RUNNER"
        if curr < best:
            runners = [i] + [j for j in range(4) if j != i]
            best = curr
    else:
        curr = f + best_three_second_leg
        if curr < best:
            runners = [i] + [0, 1, 2]
            best = curr

print(best)
for r in runners:
    print(xs[r][0])