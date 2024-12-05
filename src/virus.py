# Virus Replication
# https://open.kattis.com/problems/virus
# TAGS: queue, greedy
# CP4: 3.4f, Non Classical, Harder
# NOTES:
from collections import deque

s = input()
t = input()

qs = deque(list(s))
qt = deque(list(t))

while qs and qt and qs[0] == qt[0]:
    qs.popleft()
    qt.popleft()

while qs and qt and qs[-1] == qt[-1]:
    qs.pop()
    qt.pop()
    
print(len(qt))