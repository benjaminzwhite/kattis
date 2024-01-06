# Detailed solution for Kattis - Swap Space

[Problem statement on Kattis](https://open.kattis.com/problems/swapspace)

This is a very nice problem (indeed, the metadata says it is from the ICPC World Finals 2016), and is good practice for reasoning about greedy solutions.

I found the problem description confusing (in terms of hard drive space and size, and the reformatting operation) and so I reformulated it in terms of glasses of water, as explained below in the solution.

## Tags

greedy

## Solution

I reformulate the given problem statement as follows, in terms of glasses of water.

Note that instead of "reformatting" disks, I pretend that I **destroy a glass and build a new one from scratch** - this avoids all the confusion about which disk originally contained which data etc. and reproduces the expected behavior that is stated in the problem statement as:

*"It is not necessary to put all the data on the same drives they originally started on – in fact, this might even be impossible if some of the drives have smaller capacity with the new file system. It is also allowed for some data to end up on the extra drive."*

### Reformulation

You have a collection of glasses of different sizes which initially are **completely filled with water** with a water amount = `old` (variable name used below) e.g. in testcase with `6,1,3,3` we are saying that the first glass has `old` water amount = `6`, then second has `1` water etc.

For each glass you need to: empty its contents into *one or more* other glasses, then destroy the current glass, then build a new glass of size = `new` (variable name used below).
e.g. in testcase these are the values `6,7,5,5`.

You will buy one **extra glass** to use as a temporary container to achieve the steps described above.

The problem is asking: **"What is the smallest volume that this extra glass needs to have to allow all the operations to be performed?"**


### Reasoning

A greedy approach works: you start with the glasses which, when broken, are rebuilt as **bigger than before** i.e. which have `new > old` because these ones will result in **spare/extra capacity** when you re-pour the water from the temporary glass back.

e.g. For a given glass with `old = 100` and `new = 345`, then you will be ending up with a new glass of capacity `345` but only contributing `100` units of water to pour in to it.

In effect, this given glass can be thought of as **producing `345 - 100 = 245` spare capacity for water.**

On the other hand, a glass with `old >= new` can be thought of as **consuming, rather than producing** spare capacity for water.

Now, you sort the spare capacity **producing** `(old, new)` pairs by **increasing** `old`, since you want to greedily try to move the smallest old water
amounts because that is what requires extra glass size. By trying in this order, you never create a large extra glass before you need it (and
in all cases, you will be able to use any available spare capacity in the existing glasses first).

You tiebreak on **largest** `new` value so that you have as much new capacity available earlier rather than later.

Then, by the reverse argument of above, sort the spare capacity **consuming** pairs by **decreasing** `old`, and tiebreak on **smallest** `new` value.

## AC code

```python
n = int(input())

produce_spare_capacity = []
consume_spare_capacity = []

for _ in range(n):
    old, new = map(int, input().split())
    if old < new: # CARE! WA when use <=
        produce_spare_capacity.append((old,new))
    else:
        consume_spare_capacity.append((old,new))

# sort by SMALLEST old value, so try using SMALLEST size of the "extra glass, V"
# and tiebreak on LARGEST new value ("size of new glass") so that you have as much new capacity available earlier rather than later
produce_spare_capacity = sorted(produce_spare_capacity, key=lambda t:(t[0], -t[1]))

# vice versa for the "consume" capacity compared to the above "produce" argument
consume_spare_capacity = sorted(consume_spare_capacity, key=lambda t:(-t[1], t[0]))

max_V_of_extra_glass_needed = 0
acc_spare_capacity_in_new_glasses = 0
curr_total_avail_spare_capacity = 0 # in either the extra glass, or across all previous new glasses i..e == max_V + acc_spare

for old, new in produce_spare_capacity+consume_spare_capacity:
    # 0. if, when we try to empty this glasses old contents, we find that we don't have enough curr_total_spare_capacity
    #    then we need to increase the curr_total_spare_capacity.
    #    THE ONLY WAY TO DO THIS IS TO USE A LARGER EXTRA_GLASS SIZE, so greedily increase that extra_glass size just enough
    #    so that it will handle this glass' old_amount_of_water
    if old > curr_total_avail_spare_capacity:
        max_V_of_extra_glass_needed += (old - curr_total_avail_spare_capacity)
    # 1. empty this "glass" using some combination of the extra_glass, and all previous acc_spare_capacity - this is possible due to check in step 0.
    # 2. create the new "glass" of size new
    # 3. update the acc_spare_capacity_in_new_glasses by (new - old) since that is THE UNUSED CAPACITY CONTRIBUTED BY CURRENT NEW GLASS
    acc_spare_capacity_in_new_glasses += (new - old)
    # 4. update the curr_total_avail_spare_capacity to reflect new max_V (if it was updated) and new acc_spare (if it was updated)
    curr_total_avail_spare_capacity = max_V_of_extra_glass_needed + acc_spare_capacity_in_new_glasses

print(max_V_of_extra_glass_needed)
```