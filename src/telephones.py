# Happy Telephones
# https://open.kattis.com/problems/telephones
# TAGS: brute force
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
Brute force, also weird input format:
- useless data about "source and destination"
- also you don't get call start/end but start/DURATION for some inconsistent reason O_o
"""
def is_active(call, interval):
    sc, ec = call
    si, ei = interval
    return not (ec <= si or sc >= ei) 

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break

    calls = []
    for _ in range(N):
        _, _, sc, duration = map(int, input().split())
        calls.append((sc, sc + duration))

    for _ in range(M):
        si, duration = map(int, input().split())
        print(sum(is_active(call, (si, si + duration)) for call in calls))