# Hard Drive
# https://open.kattis.com/problems/harddrive
# TAGS: greedy, logic, proof
# CP4: 9.cons, Construction
# NOTES:
"""
See comments in code directly:
"""
n, c, b = map(int, input().split())
zs = map(int, input().split())

i = n - 1
can_flip = True

res = [None] * n
for z in zs:
    res[z - 1] = 0 # 1-indexing O_o

# NOTE: reading comprehension - the RIGHTMOST IS ALWAYS SET TO 0, the leftmost is always modifiable.
#
# Greedily pack as many 1s in between adjacent z=0 predetermined locations
#
# 0|_ _ _|0 -> 0|101|0
# 0|_ _|0 -> 0|01|0
#
# Once you flip a _ to a 1, you cannot flip adjacent to 1 (well, precisely: doing so would not increase total number of flips in string e.g.
# 0111110 and 010 have 2 flips both of them, so always best to truncate strings with '1' to minimal possible length =1 to allow 2 more flips later if needed)
# NOTE: update reading comprehension - since the rightmost is always set to 0 and leftmost is always modifiable - THE ONLY WAY YOU CAN CREATE an *ODD* number of
# flips is to set the first bit (0th index -.- he uses 1 based indexing) to 1; since otherwise all other locations would have a 0 on left and right so creating even number of flips
# For situations where c is small relative to size of string you could even have something like 111111111|00000010 where you pad up to first fixed 0 with 1's
# this is c=3 situation; but the point is that you need it to start with 1 in any case to handle odd c cases - so it's just simpler to handle index0 separately at the end once you know how many
# changes are outstanding (either 0 or 1 since it is guaranteed that a solution exists)
while i > 0:
    if c >= 2 and can_flip and res[i] == None:
        c -= 2
        res[i] = 1
        can_flip = False
    else:
        # we are either at a None location, having flipped previous cell to 1, so we don't want to flip this to 1
        # or we are at a 0 location corresponding to one of the input zs being 0; so overwriting it to 0 doesnt change res 
        # in both cases, we can now flip again on next i so toggle can_flip
        res[i] = 0
        can_flip = True
    i -= 1

if c > 0:
    res[0] = 1
else:
    res[0] = 0

print(''.join(map(str, res)))