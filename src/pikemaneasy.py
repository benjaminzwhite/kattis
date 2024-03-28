# A Vicious Pikeman (Easy)
# https://open.kattis.com/problems/pikemaneasy
# TAGS: sorting
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
Reading comprehension:

- there's no "estimations" or anything like that: the A,B,C stuff is just a DIY way for you to 
  generate some values for N exercises' durations; it is irrelevant afterwards

- "the time in minutes from contest start was added to a penalty counter" -> so ACCUMULATE the
   times taken by individual exercises to get the time_since_contest_start, and update penalty
   counter WITH THIS VALUE, time_since_contest_start, NOT THE TIME t OF THE INDIVIDUAL EXERCISE
"""
N, T = map(int, input().split())
A, B, C, tzero = map(int, input().split())

ts = [0] * N
ts[0] = tzero
for i in range(1, N):
    ts[i] = ((A * ts[i - 1] + B) % C) + 1

ts = sorted(ts)

cnt = N # initialize to assume we can solve all N exercises, we will break early otherwise
time_since_contest_start, penalty_counter = 0, 0
for i, t in enumerate(ts):
    time_since_contest_start += t
    if time_since_contest_start > T:
        # overshoot at index i means that we can solve up to index i-1, which in turn means we have solved cnt = (i-1)+1 actual exercises 
        cnt = i
        break
    else:
        penalty_counter = (penalty_counter + time_since_contest_start) % (10**9 + 7)

print(cnt, penalty_counter)