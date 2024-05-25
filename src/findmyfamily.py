# Find my Family
# https://open.kattis.com/problems/findmyfamily
# TAGS: array, stack
# CP4: 0, Not In List Yet
# NOTES:
"""
Basically find a 2-1-3 pattern in a list where 2,1,3 are not necessarily all three adjacent/contiguous in the list

e.g. with input: 100 999 9999 99999 5 4 3 2 1 77777 

a valid 2-1-3 pattern is 100,5,77777 for example
(or 100,{4/3/2/1},77777  or 9999,5,77777 etc. etc. etc.)

--- 

Confusingly the exercise description overloads the k variable name, to describe 2 different things:
1) k: number of ALL cases (exercise input)
2) k: number of VALID cases (required output)
"""
res = []

T = int(input())
for case_number in range(1, T + 1):
    n = int(input())
    xs = list(map(int, input().split()))

    stk = []
    alice = float("inf")
    for l,r in zip(xs, xs[1:]):
        stk.append(l)
        if l > r:
            while stk and stk[-1] > r:
                alice = min(alice, stk.pop())
        elif r > alice:
            res.append(case_number)
            break

print(len(res))
if res:
    for elem in res:
        print(elem)