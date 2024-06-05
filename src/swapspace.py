# Swap Space
# https://open.kattis.com/problems/swapspace
# TAGS: greedy, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/swapspace.md

---

Note: I use a "glasses of water" analogy that is explained in the link above, so need to read it
to make the variable names below meaningful O_o
"""
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