# Detailed solution for Kattis - WordSpin

[Problem statement on Kattis](https://open.kattis.com/problems/wordspin)

Nice string logic exercise: here, designing a good testcase for yourself helps solve clearly.

## Tags

string

## Solution

I spent a while trying to find a helpful testcase, used this in the end:

```
aaadaa 
fffbff
```

At first you try e.g. +5 to all:

`fffiff`

then need to adjust "backwards" i to b which now takes +7, for a total cost of 5+7 = 12

But notice that doing +5 to first block of a's:

`fffdaa`

then doing d->b in +2

`fffbaa`

then doing second block of a's as +5 also:

`fffbff`

costs 5+2+5 = 12 also.

Is this a coincidence that it's same as the "use big blocks" approach?

No: the saving that you make by grouping the 2nd block of a's with the first block of a's is exactly offset/cancelled by the opposite amount of moves that you now need to additionally make to move the intervening block (of 1x d in this case) to its target. So this property means that you should split each string into contiguous blocks of chars which are moving in the **same direction**.

e.g. 

```
adf|iy|baa
zzx|cd|zzy
+++|--|+++
```

So then consider WLOG how to treat a subcase where all chars move in same direction:

```
adf 
zzx (all need +ve moves)
```

Then the only "strategy" you can use is that you may be able to piggyback on a previous large move in the same direction that you need:

e.g. if needed is +10 +8 +3, then the way to think about it is that you "pretend" to move all of the chars by +10 (the largest in this block) but you will just stop the rotation early for the +3 and +8 block: you pay a total of +10 moves.

However, think about: +10 +8 +3 +6

Note that here you **cannot** get the +6 for free with the +10 as you "stop" at the intervening +3.

So in conclusion, it's basically a stack-based "current lowest valley, then stack pop" type exercise.

### Implementation Note

You don't need to actually implement with a stack, you only need the previous element at each step.

I left the code below with stack-related code just commented out, to see where the "stack logic" would appear.


## AC code

```python
s, target = input().split()

res = 0

# NOTE: you don't actually end up needing the stack itself, only the prev element
#stk = []

prev = 0
for c_s, c_target in zip(map(ord, s), map(ord, target)):
    delta = c_target - c_s

    # check if in same direction as previous move:
    # if NOT in same direction, cannot use previous move to piggyback:
    if not prev or (delta < 0 and prev > 0) or (delta > 0 and prev < 0):
        res += abs(delta)
    elif abs(delta) > abs(prev):
        res += abs(delta) - abs(prev)

    #stk.append(delta)
    prev = delta

print(res)
```