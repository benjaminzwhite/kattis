# Stream Lag
# https://open.kattis.com/problems/streamlag
# TAGS: logic, improve
# CP4: 1.6f, Real Life, Medium
# NOTES:
"""
TODO: IMPROVE - think about the process and see if there is a shorter solution.

---

Current implementation is to just simulate the process:
You know that all packets from pkt=1 to pkt=n are present, so can add them and their arrival times
to a dict,d, then traverse the keys using range(1,2,...) in ascending order which will be "chronologically required order".

Then for each packet, check if its arrival time is > that whatever the current time is. If yes, then have to wait DELTA time
units so add that to lag, and set current time to its arrival time.

CARE! Remember to += curr_time after each packet is processed, that is the watching time for each packet.
"""
n = int(input())
d = {}
for _ in range(n):
    time, packet = map(int, input().split())
    d[packet] = time

curr_time = 1
total_lag = 0
# all packets are present from id=1 to id=n, so process them in order that they need to appear using range(1,n+1)
for pkt in range(1, n + 1):
    if d[pkt] > curr_time:
        total_lag += d[pkt] - curr_time
        curr_time = d[pkt]
    curr_time += 1

print(total_lag)