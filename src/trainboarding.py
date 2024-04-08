# Train Boarding
# https://open.kattis.com/problems/trainboarding
# TAGS: array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
"""
CARE!

It seems that you need to handle case where people are far outside the train length
("obvious" possibility but not 100% clear when reading the given inputs section:
the position x range 0 < 10_000 is chosen to look like it will fit inside
N max < 100 and Lmax <100 ie N*L <= 10_000
but I'm guessing that there are testcases where x is huge and N,L are small)
-> So all you have to do is handle how those big x passengers move into Last Train Cabin
"""
N, L, P = map(int, input().split())

cnt = {x:0 for x in range(N + 1)}

max_dist = -1

for _ in range(P):
    x = int(input())

    q, r = divmod(x, L)
    # distance to walk
    dist = abs(L // 2 - r)
    if q > N - 1:
        dist = L // 2 + (q - N) * L + r
        q = N - 1
    max_dist = max(max_dist, dist)

    cnt[q] += 1

print(max_dist)
print(max(v for v in cnt.values()))