# Erdős Numbers
# https://open.kattis.com/problems/erdosnumbers
# TAGS: BFS
# CP4: 4.4b, SSSP, BFS, Harder
# NOTES:
"""
Reading comprehension question with unclear testcase: it's straightforward BFS but in the inputs section it says that:

"Note that some authors list a limited set of his/her coauthors; but two people are considered coauthors if either lists the other as a coauthor"

So basically if e.g. bob: [frank,alice], then it may be that bob IS ALSO COAUTHOR WITH jimmy BUT IT IS NOT LISTED IN bob:
You have to wait until jimmy: details appear, then check if jimmy: [karl, bob] <-- and in this example, we see that bob is here
"""
import sys
from collections import deque, defaultdict

final = []
d = defaultdict(list)
q = deque([("PAUL_ERDOS", 0)])
numbers = {}

for l in sys.stdin:
    k, *v = l.split()
    d[k].extend(v) # CARE! have to EXTEND d[k] because it may have already been "created" as a previous key due to COAUTHORS DATA NOT BEING COMPLETE (see NOTES)
    for k_ in v:
        d[k_].append(k)
    final.append(k)

while q:
    x, deg = q.popleft()
    if x in numbers:
        continue
    numbers[x] = deg

    for x_ in d.get(x, []):
        q.append((x_, deg + 1))

for x in final:
    print(x, numbers.get(x, "no-connection"))