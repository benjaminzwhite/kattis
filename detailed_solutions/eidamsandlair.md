# Detailed solution for Kattis - Eidam-Sand Lair

[Problem statement on Kattis](https://open.kattis.com/problems/eidamsandlair)

A really cool little logic puzzle with some interesting cases to consider.

## Tags

logic

## Solution

One way I find helps to solve this kind of puzzles is to think of the Mario Kart (or other driving games) where there is a Ghost Driver on the same track as you; you can think of you and the ghost (or, here, the elevator) as being on the same course and you can think about when you overtake them and vice versa.

The first "tricky" case to think about is when you are above the lift, call the lift, and you think that maybe you should start walking ahead:

Imagine you start at Y and lift is at L. If you call the lift while at Y, and then start walking up, **all you have done is changed initial conditions**: You are now at Y' > Y and lift is at Y.

So now imagine the lift is a ghost and travels up on its own: *whether it takes you with it or not, it will reach the surface at the same time, determined entirely by its current starting position Y*.

In other words, **if the lift ever "overtakes you" then, regardless of when you got on, it would have made sense to get in the lift at any point you could have.**

So let's list the possible cases when the lift starts below you:

+ Case where the lift starts below you:
1. Solve equations: if you get to surface by walking faster than lift does, then it never makes sense to get in lift.
2. Solve equations: if the lift gets to surface faster than you do, then **you should always wait for lift, wherever it overtakes you.** As explained above, without loss of generality you can wait at your start position.

Now let's look at the other tricky case to analyze:

It is **not** true that if lift gets to surface faster, it therefore makes sense to get in the lift:

- imagine lift at floor 1 and it takes 500 secs to climb 1 floor; if you are at floor 100 and it takes you 6 secs to climb each floor, you will exit at 600 secs and lift at 500 secs overall, but of course you shouldn't go 99 floors to lift and swap into it since it is **slower per floor** than you.

This is why, in option 2 below, you must include the option `you_to_surface` and not just the first two options `walk_to_lift`, `call_lift`.

+ Case where the lift starts ahead of you:
1. Solve equations: you get to surface by walking faster than lift does, then (**you** "overtake" the lift in this case) it never makes sense to get in lift.
2. Solve equations: the lift gets to surface faster than you do - you have 3 options, which will depend on just how fast the lift is relative to you:

- a) walk to lift, and immediately get in and do the remainder of the journey in lift
- b) call lift, wait for it, and get in from your start position (the lift is super fast)
- c) walk to surface

In the code below I've left these various cases commented also.


## AC code

```python
T = int(input())
for _ in range(T):
    Yp, Lp, Ys, Ls = map(int, input().split())

    you_to_surface = Yp * Ys

    # Case I/ Lift starts below you - careful, floor numbers are bigger when they are below
    if Lp > Yp:
        lift_to_surface = Lp * Ls

        res = min(you_to_surface, lift_to_surface)

        print(res)
    else:
        # Case II/ Lift starts above you - careful, floor numbers are bigger when they are below
        lift_to_surface = Lp * Ls
        
        # walk to lift, takes time (Yp - Lp) * Ys; then get in lift to surface
        walk_to_lift = (Yp - Lp) * Ys + lift_to_surface
        
        # call lift, takes time (Yp - Lp) * Ls + Yp * Ls
        call_lift = (Yp - Lp) * Ls + Yp * Ls
        
        # you always have the option of walking all the way - see notes for a concrete example
        res = min(walk_to_lift, call_lift, you_to_surface)

        print(res)
```