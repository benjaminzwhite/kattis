# Inflation
# https://open.kattis.com/problems/inflation2
# TAGS: interpreter, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
Just keep track of the prices "ignoring inflation" and move them around when you get a query:
lookup the "real/effective" price by removing the current value of the inflation

Also, I track the inflation PER UNIT, it keeps things simple: then, for sum, just add N * inflation_per_unit

---

There is one subtle implementation point; see comment in code below, copied here also:

cnt[x - infl_acc] -= val # CARE! this is the only tricky part:
if you naively set cnt[x - infl_acc] to 0 you will get WA due to, for example, cases where you SET CURRENT_PRICE TO CURRENT_PRICE:

i.e. imagine a testcase with just 1 query:

xs = 5 5 5 5 5 5 5 5
and
query: set 5 5

-> then if you set cnt[5-0] to 0 you "lose" all the items !!!
"""
from collections import defaultdict

N = int(input())

cnt = defaultdict(int)
total = 0
infl_acc = 0
for p in map(int, input().split()):
    total += p
    cnt[p] += 1

Q = int(input())
for _ in range(Q):
    op, *xs = input().split()
    if op == "INFLATION":
        infl_acc += int(xs[0])
    else:
        x, y = map(int, xs)
        val = cnt.get(x - infl_acc, 0)
        total += (y - x) * val
        cnt[y - infl_acc] += val
        cnt[x - infl_acc] -= val # CARE! this is the only tricky part: if you naively set cnt[x-infl_acc] to 0 you get WA due to, for example, cases where you SET CURRENT_PRICE TO CURRENT_PRICE: i.e. imagine a testcase with just 1 query: xs = 5 5 5 5 5 5 5 5 and query: set 5 5 -> then if you set cnt[5-0] to 0 you "lose" all the items !!!
    print(total + N * infl_acc)