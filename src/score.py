# Score!
# https://open.kattis.com/problems/score
# TAGS: datetime
# CP4: 1.6f, Real Life, Medium
# NOTES:
"""
Exercise is mainly date time + output formatting, probably can solve with datetime lib more elegantly but this is easier to debug
"""
n = int(input())

h_score, a_score = 0, 0
h_win_time, a_win_time = 0, 0

prev_time = 0

for query in range(n):
    team, pts, t = input().split()
    mm, ss = t.split(':')
    
    curr_time = int(mm) * 60 + int(ss)
    delta = curr_time - prev_time
    prev_time = curr_time
    
    # in the previous interval, was any team winning?
    if h_score > a_score:
        h_win_time += delta
    elif a_score > h_score:
        a_win_time += delta

    pts = int(pts)
    if team == 'H':
        h_score += pts
    else:
        a_score += pts

    if query == n - 1:
        if h_score > a_score:
            h_win_time += 32 * 60 - curr_time
        elif a_score > h_score:
            a_win_time += 32 * 60 - curr_time

winner = 'H' if h_score > a_score else 'A'

q, r = divmod(h_win_time, 60)
qq, rr = divmod(a_win_time, 60)

# output formatting
print(winner, f"{q}:{str(r).zfill(2)}", f"{qq}:{str(rr).zfill(2)}")