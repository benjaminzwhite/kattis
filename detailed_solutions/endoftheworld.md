# Detailed solution for Kattis - The End of the World

[Problem statement on Kattis](https://open.kattis.com/problems/endoftheworld)

A nice variant on the Tower of Hanoi classics.

## Tags

recursion

## Solution

The key thing to note from the problem statement is **you are told that you will always be given a state that appears in the optimal solution path**.

So you're just trying to explain/unravel the recursion steps of Tower of Hanoi:

The key say-out-loud step I found for solving is:

- "In the optimal solution, the largest disk only moves **once**: from its start position to the target position"

From that setence you can easily grasp the recursive case for N current disks: you just focus on the current largest disk, and then once it's in the right position, "pretend you delete it from the system" and consider the next largest disk etc.

Case 1:

If the largest disk is on target pole, then "delete" this largest disk and solve the state with N-1 current disks (+0 moves to total). The N-1 disks "should" have been moved to the "temp" pylon, so for the recursion the new state will START from temp, and use current "start" as its "temp" pylon:

`start, temp = temp, start` (everything else unchanged, it's as if largest disk had never existed, and you just relabel the pylons)

Case 2:

If the largest disk is NOT on target pole:

In the case where the current state is "N-1" disks on temp pole, Nth on start pole: then it will take: 1 move to move N to target, plus 2**(N-1) - 1 moves to move the (N-1) disks recursively from temp to target. **You account for these moves "now" since they will always be necessary.**

In the general case where the current state is NOT the "final step before you move disk N", you will get an extra number of steps S, corresponding to the number of steps to move N-1 disks into the state where N-1 disks are on temp pole. **But this is just what you would calculate for the "next" largest disk, if you assumed that/relabel the current "temp" (for the *largest* disk's point of view) is the "target" for the disks *before* it.** So solve the case for the N-1 disks, just swapping:

`temp, target = target, temp`

### Implementation notes

There is some reading comprehension/weird input choices in my opinion:

1. A, B, C are the labels of the pylons; A is start but **B is the target** O_o
2. the list is "backwards": the **smallest disk is described by index 0** etc.

Based on point 2, since the largest items are represented by last item in the input string, I just `list(input())` and stack pop from it.

## AC code

```python
while True:
    s = input()
    if s == 'X':
        break

    stk = list(s)

    REF = "ABC"
    start, target, temp = 0, 1, 2

    res = 0
    while stk:
        largest_disk = stk.pop()
        if largest_disk == REF[target]:
            # -- dont need to do any moves to get current largest disk into the right final position.
            # -- next largest disk is either at bottom of "temp" and needs to be moved to "target" using "start" as its temp pylon, 
            #    or is also at target already.
            start, temp = temp, start
        else:
            # "solve" the system above this largest disk:
            # there are "n-1" remaining disks (i.e. those remaining in stk[] ) that are being moved around and 
            # from the perspective of this largest disk it is *as if they have as their final target, the current TEMP pylon*
            # these moves will be added in next step of while loop, as long as you account for different target by taking:
            temp, target = target, temp
            # once they reach this, there will need to be added the moves for this current largest disk (so account for them NOW):
            # -- 1 move to move curr largest to curr target
            # -- 2**(n-1) - 1 moves to "solve tower of Hanoi" for the disks once they also reach the base case of being all on one pylon
            res += 1 + 2**len(stk) - 1 # this is just: 2**(n-1) of course, but left like this for clarify from notes

    print(res)
```