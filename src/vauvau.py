# Vauvau
# https://open.kattis.com/problems/vauvau
# TAGS: logic
# CP4: 5.3i, Modular Arithmetic
# NOTES:
"""
Statement isn't very clear about when an interval overlaps or not (ie T or T-1 needs to be <= end of dog interval etc.)
so I left print() statements used during debugging

Very similar to https://open.kattis.com/problems/semafori where we ask "are we in green light or red light part of the cycle R+G"
"""
A, B, C, D = map(int, input().split())
P, M, G = map(int, input().split())

for T in P, M, G:
    cnt = 0
    
    part_of_cycle_dog1 = (T - 1) % (A + B) # not super clear what the Time interval is inclusive/exclusive - setting T-1 passes test cases
    if part_of_cycle_dog1 >= A:
        #print("dog1 is not aggressive")
        pass
    else:
        #print("dog1 IS aggressive")
        cnt += 1
    
    part_of_cycle_dog2 = (T - 1) % (C + D)
    if part_of_cycle_dog2 >= C:
        #print("dog2 is not aggressive")
        pass
    else:
        #print("dog2 IS aggressive")
        cnt += 1
    if cnt == 0:
        print("none")
    elif cnt == 1:
        print("one")
    else:
        print("both")