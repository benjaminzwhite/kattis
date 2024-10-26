# Calculating Darts Scores
# https://open.kattis.com/problems/calculatingdartscores
# TAGS: array, brute force
# CP4: 3.2d, Three+ Nested Loops, H
# NOTES:
"""
SINGLES is the list of scores that you can hit with a single dart: it is obtained as modifier (1,2,3x) times the section score (1,2,...19,20)
We generate all possible single-dart scores, then loop over SINGLES 3 times, to see if can make the target from sum of 1,2 or 3 scores from SINGLES

On first submit - I didn't realise you are allowed <= 3 throws, so was only producing total scores that
can be formed with exactly == 3 darts, whereas some scores can be obtained with 1 or 2.
e.g. target = 2 *can* be reached with single=1, single=1, -pass- but *cannot* be reached if you must use 3 darts.

Quick fix -> add an entry (0,-1,-1) to SINGLES list (or you can take modifier from 0->3 instead, I just left my code below from first submission)
"""
target = int(input())

SINGLES = [(0, -1, -1)]
for modifier in range(1, 4):
    for section in range(1, 21):
        SINGLES.append((modifier * section, modifier, section))

res = next(((a, b, c) for a in SINGLES for b in SINGLES for c in SINGLES if a[0] + b[0] + c[0] == target), None)

if res is None:
    print("impossible")
else:
    LOOKUP = ["", "single", "double", "triple"]
    for throw in res:
        score, modifier, section = throw
        if score > 0:
            print(LOOKUP[modifier], section)