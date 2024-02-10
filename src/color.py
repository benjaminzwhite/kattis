# Coloring Socks
# https://open.kattis.com/problems/color
# TAGS: greedy, sorting, logic
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
Greedy - put socks together as long as their k-difference is <= k and the current_capacity of the machine is < c_max allowed.

Once you reach either full capacity, c, or the difference between 2 socks is > k, then must start a new machine with current sock.
"""
_, c, k = map(int, input().split())
xs = sorted(map(int, input().split()))

curr_c = 1
prev_k = xs[0]
res = 1

for x in xs[1:]:
    if x - prev_k <= k and curr_c < c:
        curr_c += 1
    else:
        res += 1
        curr_c = 1
    prev_k = x

print(res)