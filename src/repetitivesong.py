# Repetitive Song
# https://open.kattis.com/problems/repetitivesong
# TAGS: array, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
For each word you encounter in the song, look for previous occurence of it:

The distance between the 2 occurences is the "reduction" in the song length that would be caused by confusing the 2 occurences e.g.

  aaa, bbb, ccc, ddd, eee, fff, ddd, xxx, yyy, zzz <-- the distance between ddd(1) and ddd(2) is == 2
  and therefore the 2 maximal songs: aaa,bbb,ccc,(ddd),xxx,yyy,zzz can be confused where (ddd) is either ddd(1) or ddd(2)

So basically look for the *shortest distance* between 2 consecutive appearances of the same word, and *remove* this from overall length N

---

CARE! I got WA for how I was handling case where all words are distinct:

aaa,bbb,ccc -> I was producing 3 but answer wants this case to be 0
"""
N = int(input())

d = {}
res = float('inf')
for i in range(N):
    curr = input()
    delta = i - d.get(curr, -float('inf'))
    d[curr] = i
    res = min(res, delta)

# if res is not < float('inf') it has not been toggled, so HAVE NOT FOUND ANY DUPLICATE WORDS IN SONG so answer is 0
# (see notes above about how this edge case is supposed to be handled)
print(N - res if res < float('inf') else 0)