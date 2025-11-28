# Button Bashing
# https://open.kattis.com/problems/buttonbashing
# TAGS: priority queue
# CP4: 4.4a, SSSP, BFS, Easier
# NOTES:
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    n, t = map(int, input().split())
    buttons = list(map(int, input().split()))

    reachable = [float('inf')] * 3605
    reachable[0] = 0

    pq = []
    heappush(pq, 0)

    while pq:
        curr_t = pq.pop()
        for button in buttons:
            #next_t = curr_t + button
            # CARE! value is capped at 3600: reading comprehension exercise statement
            next_t = min(3600, curr_t + button)
            if 0 <= next_t and reachable[next_t] > reachable[curr_t] + 1:
                reachable[next_t] = reachable[curr_t] + 1
                heappush(pq, next_t)

    for time, moves in enumerate(reachable[t:], t):
        if moves < float('inf'):
            print(moves, time - t)
            break
