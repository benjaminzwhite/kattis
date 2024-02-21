# Bard
# https://open.kattis.com/problems/bard
# TAGS: dict
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Just updating/simulating the process, don't know if there is a smarter way.

CARE! Make sure you .copy() the big_set, don't just update the references.
Note also some tricky implementation details in code below.
"""
villagers = int(input())
evenings = int(input())

d = {i:set() for i in range(1, villagers + 1)}
curr_song = 1

for _ in range(evenings):
    _, *xs = map(int, input().split())
    if 1 in xs:
        for x in xs:
            d[x].add(curr_song)
        curr_song += 1
    else:
        big_set = set()
        for x in xs:
            big_set.update(d[x])
        for x in xs:
            d[x] = big_set.copy() # copy() !!

for k, v in d.items(): # note that dict is stable so we created the keys in order so the output will output in sorted order also
    if len(v) == curr_song - 1: # -1 because we overshoot by +1 after updating the last actual song, so the number of different songs actually sung is -1 
        print(k)