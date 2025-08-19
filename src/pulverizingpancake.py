# Pulverizing Pancake
# https://open.kattis.com/problems/pulverizingpancake
# TAGS: greedy
# CP4: 0, Not In List Yet
# NOTES:
"""
Greedy logic - if current x is 1, you always have to use a move to remove it, so:

-> look ahead at the next 3 cells: if there is more than one 1 there, it will make sense
to perform a pancake move in the middle of the range, so that you get one or two other 1's to move along
to left, right and get crushed "for free"

Illustration is clearer:

   || 1  1  1  1  1
      ^    ***
      here we will have to perform 1 pancake move anyways so, looking ahead, can we "get some others for free"?
      YES: if we first perform the pancake move at ***, the state will become:

      2  0  0  0  2
      ^
      and now performing pancake here (which we were going to do anyway) will remove 2 pokemon
      -> we also get the "right" side 1 to move, so +1 saving there also
      -> we "paid" 1 extra pancake to make the *** move. So in all we either saved +2-1 = 1 move or +1-1 0 moves
         but it's never suboptimal to do this.

---

CARE! when implementing the "right boundary condition" -> there are basically a few cases to handle,
you have things like 11[1]1 -> 1001 where [] is where the lookahead performs the pancake move ahead of the i=0 step

Consider making some testcases like 111000001 etc. to check solution handles this propagating behavior
"""
n, m = map(int, input().split())

xs = list(map(int, input()))

res = 0
for i, x in enumerate(xs):
    if x == 1:
        res += 1
        # "greedy" logic: if this x needs to be removed, i.e. if x==1, then we might as well
        # try to get some others onto this location, and remove them with the same move for free:
        if sum(xs[i + 1:i + 4]) > 1:
            if i < n - 2:
                xs[i + 1] = 0
                xs[i + 2] = 0
            if i + 3 <= n - 1 and xs[i + 3]:
                if i + 4 <= n - 1:
                    xs[i + 3] = 0
                    xs[i + 4] = 1
            res += 1

print(res)