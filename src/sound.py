# The Sound of Silence
# https://open.kattis.com/problems/sound
# TAGS: sliding window, deque, nice
# CP4: 9.slid, Sliding Window
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/sound.md
"""
from collections import deque

n, m, c = map(int, input().split())
xs = map(int, input().split())

big = deque()
small = deque()

no_silence = True

for i, x in enumerate(xs, 1):
    while big and big[0][0] <= i - m:
        big.popleft()
    while big and big[-1][1] < x:
        big.pop()
    while small and small[0][0] <= i - m:
        small.popleft()
    while small and small[-1][1] > x:
        small.pop()

    big.append((i, x))
    small.append((i, x))

    if big[0][1] - small[0][1] <= c and i > m - 1: # m - 1 since using 1 based indexing in enumerate, i.e. i >= m
        print(i - m + 1)
        no_silence = False

if no_silence:
    print("NONE")
