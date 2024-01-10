# Alphabet Spam
# https://open.kattis.com/problems/alphabetspam
# TAGS: array
# CP4: 2.2a, 1D Array, Medium
# NOTES:
"""
Place bjorn at the rightmost position and keep shifting him by 1 index leftwards

[ ... f g Bjorn] -> [ ... f Bjorn g] -> [ ... Bjorn f g]

which has the effect locally of just increasing the value of the "left-adjacent" index by exactly +1

which in turn increases the current total by (+1 * value of left-adjacent element)

so, first calculate the "sum of i*x" with Bjorn REMOVED from the list. 

Then perform this shifting for all possible indices, and track res = max(res, new_sum)

---

IMPLEMENTATION NOTES:

1. don't need to actually del Bjorn from the list - can just enumerate a filter and skip the x=0 value
2. when iterating backwards, also don't need to handle separately the x=0 value, since it will contribute +1 * 0 = 0 

CARE! think about these 2 points, not obvious (and would not be good approach for maintainable code O_o).
"""
n = int(input())

xs = list(map(int, input().split()))

# "remove" Bjorn from the list (don't need to modify list, just enumerate filter)
# and calculate the initial sum of index * value for the remaining elements in the list
initial = sum(i*x for i,x in enumerate(filter(lambda x: x != 0, xs), 1)) # CARE! 1 based indexing

res = initial

# x below is the value to the left of Bjorn as we keep shifting him leftwards
# CARE! note that we will encounter a x=0 value which is the "original" Bjorn
# which we did not physically delete from the list, but this doesn't affect calculation.
for x in xs[::-1]:
    initial += x 
    res = max(res, initial)

print(res)