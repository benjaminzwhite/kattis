# Largest Hoarding
# https://open.kattis.com/problems/largesthoarding
# TAGS: array, stack
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
A bit tricky to get the implementation without errors - I left longer variable names for this reason.

It's the classic "largest rectangle in skyline" question with a twist: the buildings have different widths 
So in the usual approach you just track indices since all widths are "1"
but here just accumulate the total width of the "candidate rectangles" as you pop from the stack
(which gets popped anytime you have a right building whose height is < stack's[-1] height
 i.e. whenever height has decreased compared to previous building)

Implementation note:

When you pop the stack you are processing stuff BEFORE this current element
then "merging the current element" into the resulting composite looking_leftwards_rectangle that you have formed.
My first implementation was trying to merge the current rectangle
(i.e. whenever you find height decreasing, and start popping left[] stack) immediately, so got subtle WA because of this
"""
def max_area_rect(bldgs):
    bldgs = bldgs + [(0, 0)] # handle last element by appending (0, 0) to actual list of buildings
    left = []
    res = 0

    for right in bldgs:
        #print(left)
        this_height, this_width = right
        additional_width_looking_leftwards = 0
        while left and left[-1][0] >= right[0]:
            adjacent_left_bldg_height, adjacent_left_bldg_width = left.pop()
            additional_width_looking_leftwards += adjacent_left_bldg_width
            area = additional_width_looking_leftwards * adjacent_left_bldg_height
            res = max(res, area)
        if this_height > 0:
            left.append((this_height, this_width + additional_width_looking_leftwards))

    return res

N = int(input())
bldgs = []
for _ in range(N):
    h, w = map(int, input().split())
    bldgs.append((h, w))

print(50 * max_area_rect(bldgs)) # need to multiply by 50 : reading comprehension in the exercise statement