# Rock Band
# https://open.kattis.com/problems/rockband
# TAGS: array, logic
# CP4: 2.2b, 1D Array, Harder
# NOTES:
"""
Iiterate column by column, add all songs in each column to a set:
Once you have as many distinct songs in the set as you have i==songs_to_play (<- which is given by how far rightwards you are in the columns)
then you know (since the songs are distinct 1 -> S and all people have S songs in some order) that the columns
to your left must consist of i copies of M songs (just draw it, you will see it straight away)
"""
M, S = map(int, input().split())
xs = []
for _ in range(M):
    xs.append([*map(int, input().split())])

u = set()
for i, col in enumerate(zip(*xs), 1):
    u.update({*col})
    if i == len(u):
        print(i)
        print(*sorted(u))
        break