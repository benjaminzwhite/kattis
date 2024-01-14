# Engineering English
# https://open.kattis.com/problems/engineeringenglish
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
import sys

seen = set()

for line in sys.stdin:
    tmp = []
    for x in line.split():
        if x.lower() not in seen:
            tmp.append(x)
        else:
            tmp.append('.')
        seen.add(x.lower())
    print(' '.join(tmp))