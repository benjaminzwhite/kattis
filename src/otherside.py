# Other Side
# https://open.kattis.com/problems/otherside
# TAGS: logic
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
See comments in code directly
It's a wolf-sheep-cabbage boat twist O_o
"""
W, S, C, K = map(int, input().split())

# 1) if both "groups" i.e. the incompatible S vs W+C groups are > K, then no matter how you fill boat there will always be something the target
# of something else on a bank
if W + C > K and S > K:
    print("NO")
elif W + C == K and S > K:
    # 2) you can move W+C to other bank, then travel back empty, then move K out of the S sheep across, then when you reach bank with W+C
    # you take those W+C back across (there are K sheep on right bank)
    # -> now when you reach leftbank, which has S' = S-K sheep, you MUST be able to take all these S' in your next journey else you will have at least one sheep on leftbank and at least one W+C to empty out
    #    of your boat, or alternatively you will not be able to empty a single space in your boat (which has W+C in it) so you are stuck and cannot move any more items across.
    # -> so in effect, need S' <= K, ie. S-K <= K, i.e. S <= 2*K
    if S <= 2 * K:
        print("YES")
    else:
        print("NO")
elif W + C > K and S == K:
    # 3) this is same case as 2) but with W+C and S roles swapped:
    if W + C <= 2 * K:
        print("YES")
    else:
        print("NO")
elif W + C == K and S == K:
    # 4) this is special case of 2) and 3), just need to shuttle across -> <- ->, one for each group + 1 back trip with empty boat
    print("YES")
else:
    # 5) either W+C < K or S < K: then whichever group has <K, you can keep them in your boat at all times while you transport the "other" group
    # even if it's only 1 unit at a time, doesn't matter.
    # e.g. if W+C is 10000 and S = 9 and K = 10, then put all 9 sheep in boat, then with 1 empty slot, keep shuttling 1 W or 1 C at a time, keeping all 9 S in boat until the 10000 W+C have crossed, then can unload the S with the boatman 
    print("YES")