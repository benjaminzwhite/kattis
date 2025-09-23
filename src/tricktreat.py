# Trick or Treat
# https://open.kattis.com/problems/tricktreat
# TAGS: ternary search
# CP4: 3.3c, Ternary Search & Others
# NOTES:
"""
TODO: Check how many times you actually need to run the ternary search?

Here, below, I hardcode it to 100 runs but can you do it programatically?

I've read in Halim CP4 book about benefits of doing it this way compared to "while diff > EPS" approach.

---

Implementation note:

For the calculations, just compare the max squared distance; then just take sqrt() once at final step for printing.
"""
from sys import stdin

while True:
    n = int(stdin.readline())
    if n == 0:
        break

    xs = []
    for _ in range(n):
        x, y = map(float, stdin.readline().split())
        xs.append((x, y))

    stdin.readline() # there are gaps between testcases O_o

    lo, hi = -200_000, 200_000
    EPS = 1e6

    delta = (hi - lo) / 3
    m1 = lo + delta
    m2 = hi - delta

    def longest_dist_in_xs(xs, guess_x):
        res = -float('inf')
        for x, y in xs:
            res = max(res, (x - guess_x) ** 2 + y ** 2) # compare squared distances, don't need to take sqrt()
        return res

    for _ in range(100):
    	# can probably optimize this by iterating once over xs and getting m1,m2 at the same time
        m1_dist = longest_dist_in_xs(xs, m1)
        m2_dist = longest_dist_in_xs(xs, m2)

        if m1_dist > m2_dist:
            lo = m1
        else:
            hi = m2

        delta = (hi - lo) / 3
        m1 = lo + delta
        m2 = hi - delta

    print(m1, longest_dist_in_xs(xs, m1) ** 0.5)