# Evening Out 2
# https://open.kattis.com/problems/eveningout2
# TAGS: brute force, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: Noticed that some Python solutions are 0.05 secs, so think about a O(1) solution?

---

Really over-ranked exercise - currently 6.5 on Kattis O_o
"""
n, x = map(int, input().split())

res = float('inf')
for d in range(1, int(n**0.5) + 1):
    if n % d == 0:
        res = min(res, abs(d - x), abs(n // d - x))

print(res)