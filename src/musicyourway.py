# Music Your Way
# https://open.kattis.com/problems/musicyourway
# TAGS: sorting
# CP4: 2.2f, Sorting, Harder
# NOTES:
"""
Implementation below relies on fact that Python sort is stable: by repeatedly
assiging songs = sorted(songs, key = lambda x: x[index_to_sort_by])
you keep the previous sort order info between each requery.
"""
d = {}

for i,x in enumerate(input().split()):
    d[x] = i

m = int(input())

songs = []

for _ in range(m):
    xs = input().split()
    songs.append(xs)

n = int(input())

for command in range(n):
    key = input()
    index_to_sort_by = d[key]
    songs = sorted(songs, key = lambda x: x[index_to_sort_by])
    print(' '.join(d.keys()))
    for s in songs:
        print(' '.join(s))
    if command != n - 1:
        print()