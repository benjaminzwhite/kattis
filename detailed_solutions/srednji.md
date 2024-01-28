# Detailed solution for Kattis - Srednji

[Problem statement on Kattis](https://open.kattis.com/problems/srednji)

A very elegant array-based algorithmic puzzle; finding the *O(n)* approach is a good exercise in algorithmic reasoning and problem reformulation.

## Tags

array

## Solution

I unlocked the thought process after reformulating to myself as follows:

"B is the median in a collection of integers, if there are as many elements less than B as there are elements greater than B in that collection".

Also, basic observation:

Any collection which does not contain B will not satisfy the requirement (of B being the median of that collection), so it makes sense to measure things relative to B in any case.

So the idea is to look at "both sides" (to the left and to the right) of B, and identify where the counts of elements (less than/greater than) B on the "left" are exactly equal to the counts of elements (greater than/less than) B on the "right". Here of course the choice of what we call "left" and "right" is arbitrary, we just want the "opposing" counts however we choose to call them.

An example makes it all clear:

### Walkthrough example

Suppose `xs = 1 10 2 9 5 | B=4 | 2 8 3 7` with `B=4` identified in its position in the list.

Find the given B within the `xs` list, say it is at index `i`.

Move "LEFT" (arbitrary WLOG) through the indices less than `i`, and accumulate the **NUMBER OF ELEMENTS** less than B and greater than B as a `+1 / -1` accumlated total (again it's arbitrary encoding - for the `left_acc` I take `-= 1` for each value `< B` and `+= 1` for each value `> B`).

At each step of previous step, increment a dict `d{}` with the **COUNT** of **HOW MANY TIMES** this `left_acc` value occurs.

So, for e.g.  `1 10 2 9 5 | B=4 | rest of xs ....`, moving leftwards from `B=4` to `5, 9, 2, 10, 1` you would have:

```
   left_acc=0 initally
   then x=5 > B=4, so left_acc -=1 = -1 -> update d[-1] += 1, so d = {-1: 1}
        x=9 > B=4, so left_acc -=1 = -2 -> update d[-2] += 1, so d = {-1: 1, -2:1}
        x=2 < B=4, so left_acc +=1 = -1 -> update d[-1] += 1, so d = {-1: 2, -2:1} 
 
 --> SO THIS d{} IS NOW SAYING THAT THERE ARE *2* LOCATIONS TO THE LEFT OF B=4 WHERE d == -1
     i.e. THERE ARE 2 LOCATIONS WHERE THE DIFFERENCE OF THE NUMBER OF ELEMENTS > B AND < B IS -1

        x=10 > B=4, left_acc -= 1 = -2 -> d[-2] += 1 so d={-1:2, -2:2}
        x=1 < B=4, left_acc += 1 = -1 -> d[-1] += 1 so d={-1:3, -2:2}
```

Now, return to original `i` where B is, and **move rightwards** this time, maintaining a `right_acc`.

**Each time you find an "opposite value" to one that appears in d{}, this defines a range where there as as many x's > B as there are x's < B.**

Going back to the example above, after processing the `1 10 2 9 5 | B=4 | rest of xs ....` left side, we have `d{}` from the "left x's" given by `d = {-1:3, -2:2}`.

Suppose then that the rest of xs is: `2 8 3 7`. Start with `right_acc = 0`.

First element `x=2 < B=4`, so `right_acc -= 1` (**CAREFUL TO "FLIP THE +1 and -1" RELATIVE TO THE left_acc STEPS SO YOU MATCH "COMPLEMENTARY PAIRS" , this way also makes it easy for lookup k with d[k] instead of taking -k**)

Now lookup in `d{}: d[right_acc = -1] = 3`, this means that there are `3` locations to the left of `B=4` which have a `left acc` of `-1`.

For clarity (see the walkthrough example) these were "obtained" at `left_idx` corresponding to `x=5,2,1`

And you can indeed check that `[5,4,2], [2,9,5,4,2] and [1,10,2,9,5,4,2]` all have an odd number of elements and have B=4 as median value because, by our construction, they have a matching number of elements that are > B and of elements that are < B.

### Implementation notes

Apart from the idea of "flipping the +1 and -1" in the encoding of the `left_acc` and `right_acc` pairs (see above, potential for confusion when re-reading code) there is one small implementation detail also:

CARE! You need to handle the fact that `[B]`, i.e. a single list with just B  in it, is a valid solution.

There is potential for missing this case, if you start counting your results from the first element "after" B when doing your processing for example. **I did this in the example walkthrough above, where I started at `2 8 3 7`, as it made the explanation easier.** But, with my code below, you do indeed need to start at the element B itself.

I handle this by initializing `d = {0:1}` representing the `acc value = 0` at `xs[i] == B`, init res = 0 also.


## AC code

```python
N, B = map(int, input().split())
xs = list(map(int, input().split()))

res = 0

# Find where the value B occurs in the input
i = xs.index(B)

# Starting left_idx to consider in first part of algorithm:
# CARE! See implementation note:
# Start with l = i - 1, SINCE WILL INIT d = {0:1} so already treated xs[i] i.e. the element B itself
# The reason you do this is because all other elements are > or < so can do if/else rather than repeatedly handle the xs == B case
l = i - 1 

d = {0:1}

# Start by moving left from the location of B (it's arbitrary choice, left/right)
left_acc = 0
while l >= 0:
    if xs[l] < B:
        left_acc -= 1
    elif xs[l] > B:
        left_acc += 1
    d[left_acc] = 1 + d.get(left_acc, 0)
    l -= 1

# Now move right from the value B and count the "pairs" that define valid intervals
right_acc = 0
while i < N:
    # CARE! dont do IF/ELSE naively beacuse you need to NOT INCREASE right_acc for i=i, i.e. when you start out xs[i] == B, so DONT CHANGE right_acc here
    if xs[i] > B:
        right_acc -= 1 # I use the "reverse encoding" of right_acc
    elif xs[i] < B:
        right_acc += 1
    res += d.get(right_acc, 0)
    i += 1

print(res)
```
