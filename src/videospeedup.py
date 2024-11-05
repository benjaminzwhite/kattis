# Video Speedup
# https://open.kattis.com/problems/videospeedup
# TAGS: simulation
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
p needs to be converted to percentage hence *0.01

Also, I prepend t=0 and append t=k as the start and end times to the [ts] list, to handle the first and last interval
"""
n, p, k = map(int, input().split())

ts = map(int, input().split())

ts = [0] + list(ts) + [k]
p = p * 0.01

res = 0
coeff = 0

for late, early in zip(ts[1:], ts):
    res += (late - early) * (1 + coeff * p)
    coeff += 1

print(res)