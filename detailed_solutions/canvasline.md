# Detailed solution for Kattis - Canvas Line

[Problem statement on Kattis](https://open.kattis.com/problems/canvasline)

This is an interesting exercise; I think that the solution (i.e. that greedy approach will work) is quite clear to get quickly, but there are some nice edge cases and implementation things to pay attention to.

After solving and rereading my code, I reimplemented a second way which I think is clearer - so I left both solutions below with comments.

## Tags

array, greedy

## Solution

### First implementation

The basic idea is easy enough: moving from left to right canvases, try adding greedily the fewest number of pegs until current canvas has 2: if you **can add the "rightmost" location**, this is always optimal since it can satisfy 2 canvases (i.e. including the "next" adjacent one) however this is **NOT ALWAYS POSSIBLE**: e.g. if "next" canvas already has 2 pegs, or has 1 peg but that peg is **already at the boundary** location etc.

The first implementation uses the above logic. Code below has some redundancy/unused variable names that I forgot to remove - for example the tracking of `uses_leftmost` isn't needed in the end.

## AC code for first implementation

```python
num_canvases = int(input())
canvases = []
for _ in range(num_canvases):
    l, r = map(int, input().split())
    canvases.append((l, r))

num_pegs = int(input())
pegs = sorted(map(int, input().split()))

flg = True # flg = False if you encounter any canvas with > 2 pegs already -> print impossible
peg_idx = 0
canvases_with_peg_info = [] # processes canvases with peg info, how many pegs for each canvas

for l, r in canvases:
    curr_cnt = 0
    uses_leftmost = False
    vals_used = set()
    if peg_idx < len(pegs) and pegs[peg_idx] == l:
        uses_leftmost = True
    while peg_idx < len(pegs) and pegs[peg_idx] < r:
        if l <= pegs[peg_idx]:
            curr_cnt += 1
            vals_used.add({pegs[peg_idx]})
        peg_idx += 1
    if peg_idx < len(pegs) and pegs[peg_idx] == r:
        curr_cnt += 1
        vals_used.add({pegs[peg_idx]})
    if curr_cnt > 2:
        print("impossible") # TODO: implement better with a sys exit or whatever
        flg = False
        break

    canvases_with_peg_info.append(((l, r), vals_used, uses_leftmost)) # TODO: should build a NamedTuple or something to be clear what the fields are
    

canvases_with_peg_info.append( ((canvases[-1][1], float('inf')), set(), True) ) # DUMMY ELEMENT TO TRIGGER LAST REAL ELEMENT PROCESSING

# Above: use canvases[-1][1] as the opening of the dummy element, this handles the cases where the last interval has a peg on its rightmost point
# as it will perform the next() search in all cases this way [since you don't care about appending the specific rightmost point for
# the last canvas, just want to append any 1,2 points needed to make up total of 2 pegs such that they DONT CLASH WITH ANY EXISTING ONES]

extra_pegs = []

# CARE! Important: need to track updates on the "right canvas" since it can be updated in the below for loop due to modifying "left canvas"
did_we_add_leftmost_to_canvas_i = [0] * (num_canvases + 10) # +10 is sentinel value

for i, (left_canvas, right_canvas) in enumerate(zip(canvases_with_peg_info, canvases_with_peg_info[1:])):
    (lc_l, lc_r), lc_vals, lc_uses = left_canvas
    (rc_l, rc_r), rc_vals, rc_uses = right_canvas

    if did_we_add_leftmost_to_canvas_i[i + 1]:
        rc_vals.add({rc_l})

    if len(lc_vals) + did_we_add_leftmost_to_canvas_i[i] == 2:
        # don't need to add any pegs
        continue

    # do len == 0 case first, as it will allow to do len == 1 straight after automatically
    if len(lc_vals) + did_we_add_leftmost_to_canvas_i[i] == 0:
        # there are 0 pegs holding this canvas so need to add 2 pegs:
        # -> for now, try adding the rightmost location, you can do this if
        # A) the right_canvas does NOT touch the left_canvas
        # B) or, the right_canvas DOES touch AND has fewer than 2 pegs 
        # [UPDATE for B): originally i thought needed extra condition: "AND doest NOT USE ITS LEFTMOST_POINT" but I think is it not needed
        # since if right_canvas used its leftmost point and the left,right canvases WERE touching then left_canvas would ALREADY HAVE 1 peg, not 0
        # so you can rule out this possibility alread
        if rc_l > lc_r or (rc_l == lc_r and len(rc_vals) < 2):
            extra_pegs.append(lc_r) # append rightmost location
            lc_vals.add({lc_r}) # update lc_vals since will check now if len(lc_vals) == 1 and will need this info
            did_we_add_leftmost_to_canvas_i[i + 1] = int(rc_l == lc_r) # update the "right canvas i+1", if it is adjacent, now that *it also has* + 1 peg in it
        # else, add lc_r - 1, can always do this since there are NO PEGS TO CLASH WITH
        else:
            lc_vals.add({lc_r - 1})
            extra_pegs.append(lc_r - 1)

    # CARE! do *not* do elif since the above == 0 check may lead to updating lc_vals
    if len(lc_vals) + did_we_add_leftmost_to_canvas_i[i] == 1:
        # Cases when you only have 1 peg on the canvas:
        # A) If this 1 peg is NOT at the rightmost, try adding the 2nd peg to be the righmost location:
        #   -> can do this if RIGHT_CANVAS shares boundary with LEFT_CANVAS and RIGHT_CANVAS has len(rc_vals) < 2
        #      or if RIGHT_CANVAS does NOT SHARE A BOUNDARY in any case
        #
        # CARE! NOTE THIS IS NOT EXACTLY THE SAME BEHAVIOR AS HE len==0 CASE ABOVE, NEED EXTRA CONDITION:
        # NEED TO CHECK THAT THE CURRENT 1 PEG IS *NOT* ON THE BOUNDARY
        # I.E. now have: or (.... and lc_r not in lc_vals)
        # YOU NEED TO CHECK:
        # if (rc_l > lc_r or (rc_l == lc_r and len(rc_vals) < 2)) and (lc_r not in lc_vals):
        # because YOU ALWAYS WANT the and (lc_r not in vals) [otherwise the code would execute with e.g. (10,20), (10000,1000010) and pegs already at 20]
        if (rc_l > lc_r or (rc_l == lc_r and len(rc_vals) < 2)) and (lc_r not in lc_vals):
            extra_pegs.append(lc_r) # append rightmost location
            lc_vals.add({lc_r}) # update lc_vals since will check now if len(lc_vals) == 1 and will need this info
            did_we_add_leftmost_to_canvas_i[i+1] = int(rc_l == lc_r) # update the "right canvas i+1", if it is adjacent, now that *it also has* + 1 peg in it
        else:
            # CARE! this is different to the len==0 case since there may be 1 peg to clash with 
            # WLOG we will add the next smallest value in the inclusive range lc_l+1, lc_r-1 [be careful to avoid boundaries!] that does not already appear in lc_vals
            peg_location = next(x for x in range(lc_l + 1, lc_r - 1 + 1) if x not in lc_vals) # I wrote: lc_r-1 + 1 just to be explicit about the allowed range
            lc_vals.add({peg_location})
            extra_pegs.append(peg_location)

if flg:
    print(len(extra_pegs))
    print(*extra_pegs)
```

### Second implementation

Here I rewrote to streamline the first approach.

Instead of carrying the vals around with you in a set() etc. rework of first approach, note that if you always **come in from the rightmost value** and keep adding until `cnt[current_canvas] == 2` you handle the "x not in vals" type logic that I had implemented in first approach.

Since the greedy guess of the rightmost possible canvas point is always the "startpoint", which you modify if the "next_canvas" has > 2 pegs already, then always starting with greedy guess, and decrementing it makes sense (I was trying to increment from leftmost canvas point).

Therefore, since `N` is small, you can just do a lookup of "original_pegs" and "new_pegs_added" instead of implementing the logic/control loops locally for each canvas:

Just try adding pegs and checking that they are

1. either **NOT** in the original pegs or
2. **NOT** in the newly added pegs either

If so, the greedy guess (or the greedy-1,-2,-3, ... depending on how far you go) will always work.

## AC code for second implementation

```python
N = int(input())

canvases = []
for i in range(N):
    l, r = map(int, input().split())
    canvases.append((l, r))

p = int(input())
PEGS = list(map(int, input().split())) # ORIGINAL_PEGS

cnt = []
peg_idx = 0
flg = 1
# exactly same as 1st version, but here creating a cnt array with "how many pegs are in curr_canvas -> ans: curr_cnt"
# instead of carrying around the actual values vals=set(4,515,15) etc in the 1st version
for l, r in canvases:
    curr_cnt = 0
    while peg_idx < p and PEGS[peg_idx] < r:
        if l <= PEGS[peg_idx]:
            curr_cnt += 1
        peg_idx += 1
    if peg_idx < p and PEGS[peg_idx] == r:
        curr_cnt += 1
    if curr_cnt > 2:
        flg = 0
    cnt.append(curr_cnt)

cnt += [0, 0, 0, 0, 0] # some sentinel values in the lookup to avoid index errors (see later due to i+1 lookup)

PEGS = set(PEGS) # convert to set for lookup in the next() step below in while loop
TO_ADD = set()
for i, (l, r) in enumerate(canvases):
    # this changes relative to first version: instead of the did_we_add_leftmost_to_canvas_i array
    # which only requires looking "locally" at previous canvas to see whether the boundary peg was added,
    # here we just LOOKUP IN TO_ADD IF THE BOUNDARY VALUE HAS BEEN ADDED SO FAR:
    # what is the boundary value? : well, if it exists and is indeed a boundary between 2 canvases, then it will
    # appear as the LEFTMOST EDGE of a later canvas -> so check: "if l in TO_ADD"
    # -> this means that we need to update count of how many pegs are in current canvas (old cnt[i] is how many ORIGINAL_PEGS)
    #    and we +=1 cnt[i] to include the NEWLY ADDED BOUNDARY PEG
    if l in TO_ADD:
        cnt[i] += 1

    greedy = r
    # see 1st version - the restriction on using the greedy guess is whether the next_canvas already has 2 or more pegs,
    # OR whether the next_canvas has 1 peg which is on the boundary: BUT THIS LATER CONDITION IS NOW HANDLED BY HAVING LOOKUP OF PEGS AND TO_ADD PEGS
    # since we know whether the eventual boundary peg exists or not (if it does it is in PEGS so we will NOT add it, see the next() loop below)
    if cnt[i + 1] >= 2: # NOTE: cnt has sentinel length of +5 or w/e so will handle index error ok
        greedy -= 1 # can NOT use the rightmost since next canvas already as 2 or more pegs assigned
    
    while cnt[i] < 2:
        # see above, always come in from rightmost (greedy guess) downwards
        # NOTE: I reread statement, the canvases all have size at least 10 so either there are already cnt[i] >= 2 pegs so loop won't enter or
        # you have < 2 pegs, so there are at least 10 - 2 = 8 vals for the next() below to add, so shouldn't get any errors:
        TO_ADD.add(next(x for x in range(greedy, -1, -1) if x not in PEGS | TO_ADD))
        cnt[i] += 1

if flg:
    print(len(TO_ADD))
    print(*TO_ADD)
else:
    print("impossible")
```