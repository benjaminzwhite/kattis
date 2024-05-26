# King's Decree
# https://open.kattis.com/problems/kingsdecree
# TAGS: array, sorting, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
Nice little exercise. While debugging I came up with some testcases:
tried xs = 15, ls = 12 and noticed I was returning 12 rather than 15 -> realised I wasn't handling END OF ARRAY PROCESSING
i.e. cases where you still have excess leftover at last element (in this case, extreme case where there is only 1 element so it is the last)
-> QUICK FIX: after sorting ls to L, append(float("inf")) so that "last element" always results in triggereing the redistribution 
   of whatever leftover excess there is at tat point
"""
T = int(input())
for _ in range(T):
    n = int(input())
    xs = list(map(int, input().split()))
    ls = list(map(int, input().split()))

    excess = 0
    for x, l in zip(xs, ls):
        excess += x - l # noticed after submitting that excess variable in the end is just sum(xs) - sum(ls) O_o 

    L = sorted(ls)
    res = L[0]
    L.append(float("inf")) # trigger end of array processing if still have excess (without this, test case like xs=15, ls=12 will return 12 rather than 15, since excess of 3 will not be redistributed)
    
    for acc_q, (fst, snd) in enumerate(zip(L, L[1:]), 1):
        # if have enough to raise all previous cats (there are acc_q of them) to snd's min level, do so:
        delta = (snd - fst) * acc_q
        if delta <= excess:
            res = snd
            excess -= delta
        # if not, fairly divide the remaining excess among the acc_q poorest to raise their levels as high as possible
        # (nb, if we have reached this point, then the acc_q poorest all currently have wealth level == fst, since we have been able to raise the acc_q
        # poorest to snd's level repeatedly until now)
        else:
            res = fst + (excess // acc_q)
            break

    print(res)