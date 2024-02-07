# Watering Grass
# https://open.kattis.com/problems/grass
# TAGS: greedy, sorting, nice
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
Nice twist on interval covering; left clear variable names below.

In a few places you should really use integer comparisons e.g. 2*r > w instead of r > w/2 (best practice).
"""
while True:
    try:
        n, l, w = map(int, input().split())
        intervals = []

        for _ in range(n):
            x, r = map(int, input().split())
            if r > w / 2: # <= w / 2 doesnt create a finite interval (at most glances the edge of the lawn at a point)
                horiz = (r * r - (w / 2) * (w / 2)) ** 0.5
                intervals.append((x - horiz, x + horiz))

        intervals = sorted(intervals)

        curr_right = 0
        cnt = 0
        i = 0

        while curr_right < l:
            extended = False
            furthest_right = 0
            while i < len(intervals): # CARE! len(intervals) not n, since dont append all n sprinklers to intervals
                this_left, this_right = intervals[i]
                if this_left < curr_right:
                    furthest_right = max(furthest_right, this_right)
                    i += 1
                    extended = True
                else:
                    break
            
            if not extended: # performed a loop and was not able to extend furthest_right without forming a gap in the coverage
                cnt = -1
                break
            
            curr_right = furthest_right
            cnt += 1

        print(cnt)
    
    except EOFError:
        break