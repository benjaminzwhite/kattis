# Simple Solitaire
# https://open.kattis.com/problems/simplesolitaire
# TAGS: stack
# CP4: 0, Not In List Yet
# NOTES:
"""
Reading comprehension + hard to clear up exercise statement/debug with only 1 testcase.
I think that's why it has high difficulty rating.

Basically the priority is:
- Check if any 4-delete operations occur, IF SO RETURN TO START OF PILE <- THIS IS BADLY EXPLAINED, YOU *DON'T* KEEP MOVING THROUGH THE PILE
- If not 4-delete, check if any 2-delete operations, IF SO RETURN TO START OF PILE
- If neither, add next card

So basically ANY operation makes you start at top all over again

---

Implementation notes:

Implemented as-is above; doing 2 passes through entire stack for each card added

I guess can do 1 pass by recording "best move" (either 4,2 or 0 delete), then perform, then loopwhile best was 4 or 2
and stop when best was 0 (then move to next card)
"""
xs = []
for _ in range(4):
    xs.extend(input().split())

stk = []
for x in xs:
    stk.append(x)
    flg = True
    while flg:
        i_max = len(stk) - 1
        modif = False
        for i in range(i_max, 2, -1):
            if stk[i][0] == stk[i-3][0]:
                del stk[i-3:i+1]
                modif = True
                break
        if not modif:   
            for j in range(i_max, 2, -1):
                if stk[j][1] == stk[j-3][1]:
                    del stk[j]
                    del stk[j-3]
                    modif = True
                    break
        if not modif:
            flg = False

print(len(stk), *stk)