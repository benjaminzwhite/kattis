# Platform Placing
# https://open.kattis.com/problems/platformplacing
# TAGS: greedy
# CP4: 0, Not In List Yet
# NOTES:
"""
Extend current platform as much as possible without caring about later ones.

See code for the 3 possible options for each platform when you greedily extend it.

Also: each platform must be of size mn at least, so need to always check r-l >= mn, as the if statement, and also
have 1 of the 3 options being that next platform is of size at least mn - i.e. cant extend rightwards if that
would create a "next" platform of size < mn

---

Implementation notes:

You can implement the numerical stuff a bit better without using float division /2 etc.
but code below is AC and it's clearer to read/interpret.
"""
N, mn, mx = map(int, input().split())

foundations = []
for _ in range(N):
    foundations.append(int(input()))

foundations = sorted(foundations) + [float('inf')] # trigger last element processing with dummy rightmost foundation

res = 0
prev_rightmost = -float('inf') # trigger first element processing: there is no prev_rightmost for first foundation, so can extend it leftwards as much as you want: only 2 rather than 3 constraints for this element (see below for list of 3)
for l, r in zip(foundations, foundations[1:]):
    if r - l < mn:
        res = -1
        break
    else:
        # try to extend current platform as much as possible:
        # 3 options:
        # -either can extend up to mx size without bumping into previous platform or next platform, so mx/2 half_size
        # -bump into previous (greedy sized) platform, which has its right edge at previous_rightmost: this means curr_platform has half_size = l-prev_rightmost
        # -bump into next platform, which MUST HAVE A SIZE mn AT LEAST, so this will impose curr_platform half_size of at most r - l - mn/2 <- to account for the next platforms size mn at least and avoid bumping into its LEFT side
        half_size = min(mx / 2, l - prev_rightmost, r - mn / 2 - l)
        prev_rightmost = l + half_size
        res += 2 * half_size

print(int(res)) # using floats about /2 0.5 etc so need to cast to int