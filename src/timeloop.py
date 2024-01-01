# Stuck In A Time Loop
# https://open.kattis.com/problems/timeloop
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
import sys

for line in sys.stdin:
    N = int(line)
    for i in range(1, N+1):
        print(f"{i} Abracadabra")