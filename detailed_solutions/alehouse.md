# Detailed solution for Kattis - Alehouse

[Problem statement on Kattis](https://open.kattis.com/problems/alehouse)

A "priority queue question" that can be alternatively solved "analytically" with some logic and a change of perspective.

## Tags

logic, sorting

## Solution

The exercise is a twist of the standard "most overlapping intervals"-type interview questions: the usual approach is that you +1 for each "start/open" of an interval and -1 for each "end/close" and take `max(curr, res)` each step.

Here the fact that you have a "window of size k" is the twist.

Thinking geometrically, there is a clever way to solve it: first, draw the intervals as you would standard way, say solid lines, `____` on paper.

Then (hard to draw in ASCII) imagine **extending each of the "real" intervals by an amount `k`.**

So with the testcase given, you end up with:

```
 5  6  7  8  9  10 11
 _____________ ------   <== here the real ___ interval is from 5 to 9, add k=2 --- at the end to reach 11 "effective"
       ____-------

etc.
```

Now do the standard approach on these "effective intervals" and find the **"effective time" `t` where there are the most overlapping**
(with the testcase, this is `t=10`, with `4` overlapping intervals `(1,8), (5,9), (7,8), (10,10)` all are intersected by `t=10` when you add `k=2` to them)

But what does this mean in terms of the "real exercise" ? It means that if you **step back `k=2` steps from `t=10` to `t=8`**, then you know that there
are, in turn, the same `4` intervals that must have at least one "real point" between `k=8` and `k=10`.

You don't need to find *where* the minimum occurs, but this reasoning shows that there is a 1-to-1 correspondence between "most overlapping **effective** intervals" and "highest number of overlapping **real** intervals if you are allowed a window of size `k`".

**I left more comments in AC code below.**


## AC code

```python
n, k = map(int, input().split())

xs = []
for _ in range(n):
    l,r = map(int, input().split())
    # NOTE: use op = 1, -1 to determine whether we will increase or decrease the "open/close interval counter"
    xs.append((l, 1)) 
    xs.append((r + k, -1)) # prolong each person's real interval by k to create an effective interval ending at r+k instead

# sortkey below places ARRIVALS (+1) before DEPARTURES (-1) in case of a tie on the arrival time, x. 
# (since you are allowed to "count the person on the way out" you CAN increment first with the new arrival
# so that the total people in shop is BIGGER+1 then SMALLER-1 so that you reach the bigger total first)
xs = sorted(xs, key=lambda x:(x[0], -x[1]))

most = 0
people = 0 # effective people at the current effective time point
for x_eff, op in xs:
    people += op
    if people > most:
        most = max(most, people)

print(most)
```