# Pyramid Construction
# https://open.kattis.com/problems/pyramidkonstruktion
# TAGS: mathematics, greedy, logic
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
Draw it:

For each 2 <= h <= H you need 2,4,6,8... of the "fours blocks"

So to make height H you need the sum: S = 2+4+6+8... of the "fours blocks"
i.e. S = 2 * (H * (H-1) // 2) == H*(H-1)

You can greedily convert the "twos" you already have into "fours" by twos//2

You need 1 "twos" for the top of the pyramid at h==1 layer
(see lines below: "twos_needed = 1 if twos == 0 else 0")
"""
H, twos, fours = map(int, input().split())

if fours >= H * (H - 1):
    tmp_twos = 1 if twos == 0 else 0
    print(tmp_twos, 0)
else:
    convert = min(((H * (H - 1)) - fours), twos // 2)
    fours += convert
    twos -= 2 * convert

    twos_needed = 1 if twos == 0 else 0
    fours_needed = H * (H - 1) - fours 

    print(twos_needed, max(0, fours_needed))