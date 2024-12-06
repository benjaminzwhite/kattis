# Radio Commercials
# https://open.kattis.com/problems/commercials
# TAGS: range sum
# CP4: 3.5a, Max 1D/2D Range Sum
# NOTES:
"""
It's Kadane's algorithm [3.5a, Max 1D/2D Range Sum is category on CP4 site]
the twist is that you have to -P where P is the cost of making the advert
(so the "effective" value of each x is actually rescaled to x-P each time)
"""
N, P = map(int, input().split())

xs = map(int, input().split())

best, prev = -float('inf'), -float('inf')

for x in xs:
    curr = x - P + max(0, prev)
    best = max(best, curr)
    prev = curr

print(max(best, 0)) # in case best is still -float('inf') i.e. not worth taking anything in the xs values