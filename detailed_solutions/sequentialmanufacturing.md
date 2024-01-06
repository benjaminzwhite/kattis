# Detailed solution for Kattis - Sequential Manufacturing

[Problem statement on Kattis](https://open.kattis.com/problems/sequentialmanufacturing)

This is a really cool problem, because you can solve it "immediately" if you have a geometric insight; otherwise you can reason about it logically.

Here I included the logical reasoning first, then I share the geometric point of view afterwards.

## Tags

logic

## Solution

### Logical reasoning approach

Imagine only 2 objects and suppose there is only 1 machine in the chain:

**The best you can theoretically do is to to adjust the sending time of object #2 so that it enters the machine just as object #1 exits.**

(i.e. thereby ensure 0 waiting time at machine #1). You do this by delaying by exactly `T_machine`; so in other words the total result time has
an additional penalty cost of `1 object * T_machine`.

Suppose now there are 2 objects and several machines; how does the above generalise?

Let the machine times be e.g. `7,99,45` mins respectively.

To ensure the condition we identified earlier (for the case of 2 objects and only 1 machine) applies here to the first machine, you delay sending object #2 by 7 minutes - it therefore enters first machine just as object #1 is exiting it.

But now once object #2 exits first machine, **it will now have to wait for object #2 to exit the 2nd machine** - since it entered it 7 minutes ago, you will be waiting for 99-7 = 92 minutes. But note that you had already delayed sending object #2 by 7 minutes, so to avoid any delay at machine 2, you may as well have just delayed 99 minutes in the first place.

Finally, and this is the key observation: once object #2 leaves machine 2 after 99mins it **does not have to wait for any machines "ahead" whose processing time is <= 99 minutes**.

In other words, the optimal strategy is to "delay sending next package by T minutes where T is the amount taken by slowest machine", because this is
what will satisfy the requirement of having object #2 never having any wait time and entering "machine with max T", i.e. the slowest machine, just as object #1 exits it.

This argument applies to objects "pairwise/locally" so it's the same requirement for object 2 -> 3, 3 -> 4 etc.

So in general the optimal strategy is sending objects into the machine chain "periodically" with a delay of max T between each sending after the first object.

### Geometric insight

Visualize the sequence of machines as a line made up of linear segments each of length = machine_time_i

e.g. `______|___|__________________|___|_|_______________________`

Visualize the objects as a lattice of points, with the first object placed just before the first machine:

e.g. `.....______|___|__________________|___|_|_______________________`

The requirement is a geometric spacing requirement: you want to dilate the 1d lattice of points (the send times of the objects) to the smallest possible spacing such that **no segment contains more than one point** (as this corresponds to 2 or more objects in the same machine).

e.g. `|____._____._____.__| <- bad, 3 points in this particular segment`

e.g. `|________.___| <- good, only 1 point in this particular segment`

So clearly you must dilate the 1d lattice until the spacing between the points is at least as large as the size of the largest segment:

solution: `.    .    .    .__|_|____|__ <- good, here the spacing of 4 between the points corresponds to size of largest segment |____|`

Now when you "push" the lattice through the sequence of machines, there will never be 2 points in the same segment.

The total time taken is thus the length of the sequence of machines plus the (P-1) gaps between the P points, each of length max T.

## AC code

```python
N, P = map(int, input().split())
ts = list(map(int, input().split()))
ks = map(int, input().split()) # unused O_o

#     v-- first object goes through unencumbered in time sum(ts)
res = 1 * sum(ts) + (P-1) * max(ts)
#                     ^___ remaining P-1 objects are each sent with a delay of max_machine_time after the first one
print(res)
```