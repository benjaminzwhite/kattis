# Thore's self-esteem
# https://open.kattis.com/problems/thore
# TAGS: string
# CP4: 0, Not In List Yet
# NOTES:
"""
See comment/UPDATE in code below - the handling of the following edge case/reading comprehension:

You are supposed to say that Thore sucks if ThoreHusfeld (WITH NO LAST T)
appears even though in such a case you might think that ThoreHusfeldt (WITH LAST T)
could be a unique prefix
"""
n = int(input())

REF = "ThoreHusfeldt"
prefix_len = 0

flg = True
for case in range(1, n + 1):
    curr = input()
    if case == 1 and curr == REF:
        print("Thore is awesome")
        flg = False
        break
    elif curr != REF:
        i = 0
        while i < min(len(curr), len(REF)) and REF[i] == curr[i]:
            i += 1
        if i >= len(REF) - 1: # UPDATE: WAS FAILING BECAUSE YOU ARE SUPPOSED TO RETURN Thore sucks if ThoreHusfeld is in list, even if ThoreHusfeldt is not (I did not have the -1 before which was causing W.A.)
            print("Thore sucks")
            flg = False
            break
        prefix_len = max(prefix_len, i)
    elif curr == REF:
        break

if flg:
    print(REF[:prefix_len + 1])