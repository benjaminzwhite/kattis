# Job Switching
# https://open.kattis.com/problems/jobbyte
# TAGS: array, mathematics, logic
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
This is the classic "minimum number of swaps needed to sort an array" question.

---

For each element, consider the cycle formed by going to its "correct index" e.g.
             _____
            |     v
 xs =    2  4  3  1     here starting at x=2, the cycle "swap x out of place to its correct index, and repeat" goes (2,4,1)   
         |__^     |     then only leftover element is x=3 which is in correct position/index, so its cycle is (3)
                  |     => EACH CYCLE REQUIRES len(cycle) - 1 SWAPS TO SORT, so total res = sum(len(cycles) - 1)
         ^________|
"""
N = int(input())
xs = list(map(int, input().split()))

processed = set()
res = 0
for i, x in enumerate(xs, 1):
    cycle_len = 0
    while x != i and x not in processed: # this is generating the cycle to which the current element, x, belongs e.g (2,4,1) above
        processed.add(x)
        x, i = xs[x - 1], x
        cycle_len += 1
    res += max(0, cycle_len - 1) # max(0, cycle_len-1) handles case when cycle_len = 0 i.e. i==x already

print(res)