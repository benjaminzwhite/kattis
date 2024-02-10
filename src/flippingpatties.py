# Flipping Patties
# https://open.kattis.com/problems/flippingpatties
# TAGS: array, logic, nice
# CP4: 2.2b, 1D Array, Harder
# NOTES:
"""
Nice little exercise:

Work BACKWARDS from each "customer desired time" - this imposes 3 needed actions:
- one at time t
- one at time t-d
- one at time t-2*d (present to customer, flip, place on grill initially respectively)

So count how many actions are needed for each time t.
Since each chef can perform 2 actions per unit time, then the number of chefs needed is the ceil of max(time)/2

Implementation note:

I was getting some issues when using ceil of max/2 etc so basically it's sum of divmod(value, 2)
e.g. if 7 actions needed you need 7//2 + 7%2 = 4 chefs
"""
from collections import defaultdict

d = defaultdict(int)

n = int(input())

for _ in range(n):
    delta, t = map(int, input().split())
    d[t] += 1
    d[t - delta] += 1
    d[t - 2 * delta] += 1

res = max(sum(divmod(v, 2)) for v in d.values())

print(res)