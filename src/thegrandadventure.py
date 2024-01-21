# The Grand Adventure
# https://open.kattis.com/problems/thegrandadventure
# TAGS: array
# CP4: 2.2j, Stack
# NOTES:
"""
Didn't implement early break - I just go through all strings to the end
"""
for _ in range(int(input())):
    s = input()
    pairings = {'b':'$','t':'|','j':'*'}
    stk = []
    flg = True
    for c in s:
        if c not in '.btj':
            stk.append(c)
        elif c != '.':
            if not stk or stk.pop() != pairings[c]:
                flg = False

    if not stk and flg:
        print("YES")
    else:
        print("NO")