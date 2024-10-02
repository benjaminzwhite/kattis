# Integer Lists
# https://open.kattis.com/problems/integerlists
# TAGS: interpreter
# CP4: 2.2l, List/Queue/Deque
# NOTES:
"""
Weird input format: input is passed as a STRING: "[3,35,135]" which you have to parse.
Since n=0 is allowed, you can end up having to parse "[]" as input string

I had hardcoded a n=0 "error" clause but it seems like it has a test with n=0 and commands like "RRRR" so rotating an empty list - oh well O_o
"""
T = int(input())

for _ in range(T):
    s = input()
    n = int(input())
    tmp = input()
    
    xs = tmp[1:-1].split(",") # input format O_o - could use AST instead I guess
    rev = 0 # we initially are dropping from front of list, so "reverse" boolean is False (use 0 and 1 for XOR based switching, and indexing in res later)
    l, r = 0, n - 1
    flg = True
    
    for c in s:
        if c == 'R':
            rev ^= 1
        elif c == 'D':
            if l > r:
                print("error")
                flg = False
                break
            if not rev:
                l += 1
            else:
                r -= 1
    
    if flg:
        res = xs[l:r+1][::1-2*rev] # 1 - 2 * rev: if rev is True=1 then -> 1-2*rev = 1-2 = -1 so [::-1] reverses string. If rev=False=0 then 1-2*rev = 1.
        print(f"[{','.join(res)}]")