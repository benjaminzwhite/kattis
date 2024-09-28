# Pairing Socks
# https://open.kattis.com/problems/pairingsocks
# TAGS: stack, logic
# CP4: 2.2j, Stack
# NOTES:
"""
You are allowed to use a 3rd operation (pop from pile #2 and put back on top of pile #1) but this seems to be a Gotcha/red herring, since this
operation never makes sense to perform - if e.g. top of pile #2 is _ // FF and you pop it back to pile #1 to get F // F in order to
subsequently pair off the two F's then this means at some point previously there was already a situation where F//F was the state and you
popped from #1 to get _ // FF, but clearly you could have - at that step - already paired them off from the top of their piles.

(Proof by contradiction that you will never need to "undo from pile #2 to pile #1")
"""
n = int(input())

xs = list(map(int, input().split()))

stk = []
cnt = 0

while xs:
    if stk and stk[-1] == xs[-1]:
        cnt += 1
        xs.pop()
        stk.pop()
    else:
        tmp = xs.pop()
        stk.append(tmp)
        cnt += 1

if stk: # if you still have unpaired socks in the destination stack/pile #2 then task is impossible
    print("impossible")
else:
    print(cnt)