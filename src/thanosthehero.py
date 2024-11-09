# Thanos the Hero
# https://open.kattis.com/problems/thanosthehero
# TAGS: array, logic
# CP4: 3.2i, Math Simulation, Harder
# NOTES:
"""
Not clear from instructions if the first population (leftmost) is allowed to reach 0 or must be 1 (I submitted and my version passed but still not sure)

---

Insight is that it's easier to move Right -> Left, then the "adjustment requirement" is always local.

The "previous" (remember we are Right -> Left) value is the only one that constrains the current one, x, since if we
reach x then the values from previous->the right are assumed to be in ascending order so there is never any element
greater than the current value of prev that needs to be tracked.
"""
N = int(input())
xs = list(map(int, input().split()))

prev = float('inf') # dummy to start, so that first element is always < prev
res = 0
flg = True

for x in xs[::-1]:
    if x < prev:
        prev = x
    elif x >= prev:
        need_to_remove = x - prev + 1
        if need_to_remove > x:
            print("1")
            flg = False
            break
        else:
            res += need_to_remove
            prev = prev - 1

if flg:
    print(res)